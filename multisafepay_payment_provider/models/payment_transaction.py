# Part of Odoo. See LICENSE file for full copyright and licensing details.

import logging
import pprint
import uuid

import requests

from werkzeug import urls

# from odoo.custom_addons.multisafepay_payment_provider.controllers.main import MultisafepayController
# from odoo.addons.payment.const import CURRENCY_MINOR_UNITS
# from odoo.addons.payment_mollie import const
# from odoo.addons.payment_mollie.controllers.main import MollieController

from odoo import _, models
from odoo.exceptions import ValidationError

_logger = logging.getLogger(__name__)

class PaymentTransaction(models.Model):
    _inherit = 'payment.transaction'

    def _get_specific_rendering_values(self, processing_values):
        """ Override of payment to return multisafepay-specific rendering values.
        Note: self.ensure_one() from `_get_processing_values`
        :param dict processing_values: The generic and specific processing values of the transaction
        :return: The dict of provider-specific rendering values
        :rtype: dict
        """

        reference_id=processing_values['reference']

        url = "https://testapi.multisafepay.com/v1/json/orders?api_key=832853d17d01547d6fbdad4c1e75573c426895ef"

        payload = {
                "payment_options": {
                    "close_window": False,
                    "notification_method": "POST",
                    "notification_url": "https://www.example.com/webhooks/payment",
                    "redirect_url": "http://localhost:8020/payment/multisafepay/return",
                    "cancel_url": "https://www.example.com/order/failed",

                },
                "customer": {
                    "locale": "en_US",
                    "disable_send_email": False
                },
                "checkout_options": {"validate_cart": False},
                "days_active": 30,
                "seconds_active": 2592000,
                "type": "",
                "gateway": "",
                "order_id": reference_id,
                "currency": "EUR",
                "amount": 1000,
                "description": "product description"
        }
        headers = {
            "accept": "application/json",
            "content-type": "application/json"
        }
        response = requests.post(url, json=payload, headers=headers)
        print(response.text)

        result=response.json()
        payment_url=result['data']['payment_url']
        return {'api_url': payment_url}

    def _get_tx_from_notification_data(self, provider_code, notification_data):
        """ Override of payment to find the transaction based on multisafepay data.
        :param str provider_code: The code of the provider that handled the transaction
        :param dict notification_data: The notification data sent by the provider
        :return: The transaction if found
        :rtype: recordset of `payment.transaction`
        :raise: ValidationError if the data match no transaction
        """

        tx = super()._get_tx_from_notification_data(provider_code, notification_data)
        if provider_code != 'multisafepay' or len(tx) == 1:
            return tx

        tx = self.search(
            [('reference', '=', notification_data.get('transactionid')),('provider_code', '=', 'multisafepay')]
        )

        if not tx:
            raise ValidationError("multisafepay: " + _(
                "No transaction found matching reference %s.", notification_data.get('transactionid')
            ))
        return tx

    def _process_notification_data(self, notification_data):
        """ Override of payment to process the transaction based on multisafepay data.

        Note: self.ensure_one()

        :param dict notification_data: The notification data sent by the provider
        :return: None
        """
        super()._process_notification_data(notification_data)
        if self.provider_code != 'multisafepay':
            return

        endpoint= f"/orders/{notification_data.get('transactionid')}?api_key={self.provider_id.multisafepay_api_key}"

        payment_data = self.provider_id._multisafepay_make_request(endpoint,
            f'/payments/{self.provider_reference}', method="GET"
        )


        # Update the payment state.
        payment_status = payment_data.get('data',{}).get('status')
        if payment_status == 'completed':
            self._set_done()

        elif payment_status in ['initialized','expired', 'canceled', 'failed']:
            self._set_canceled("multisafepay: " + _("Cancelled payment with status: %s", payment_status))
        else:
            _logger.info(
                "received data with invalid payment status (%s) for transaction with reference %s",
                payment_status, self.reference
            )
            self._set_error(
                "multisafepay: " + _("Received data with invalid payment status: %s", payment_status)
            )
