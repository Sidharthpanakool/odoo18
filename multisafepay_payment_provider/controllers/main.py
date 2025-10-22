# Part of Odoo. See LICENSE file for full copyright and licensing details.

import logging
import pprint

from odoo import http
from odoo.exceptions import ValidationError
from odoo.http import request

_logger = logging.getLogger(__name__)


class MultisafepayController(http.Controller):
    _return_url = '/payment/multisafepay/return'
    _webhook_url = '/payment/multisafepay/webhook'

    @http.route(
        _return_url, type='http', auth='public', methods=['GET', 'POST'], csrf=False,
        save_session=False
    )
    def multisafepay_return_from_checkout(self, **data):

        _logger.info("handling redirection from Multisafepay with data:\n%s", pprint.pformat(data))
        request.env['payment.transaction'].sudo()._handle_notification_data('multisafepay', data)
        return request.redirect('/payment/status')





    # @http.route(_webhook_url, type='http', auth='public', methods=['POST'], csrf=False)
    # def multisafepay_webhook(self, **data):
    #     """ Process the notification data sent by multisafepay to the webhook.
    #
    #     :param dict data: The notification data (only `id`) and the transaction reference (`ref`)
    #                       embedded in the return URL
    #     :return: An empty string to acknowledge the notification
    #     :rtype: str
    #     """
    #     _logger.info("notification received from multisafepay with data:\n%s", pprint.pformat(data))
    #     try:
    #         request.env['payment.transaction'].sudo()._handle_notification_data('multisafepay', data)
    #     except ValidationError:  # Acknowledge the notification to avoid getting spammed
    #         _logger.exception("unable to handle the notification data; skipping to acknowledge")
    #     return ''  # Acknowledge the notification
