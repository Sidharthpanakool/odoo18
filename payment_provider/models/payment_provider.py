from ast import literal_eval
from email.policy import default
# Part of Odoo. See LICENSE file for full copyright and licensing details.

import json
import logging
import pprint
import requests

from datetime import timedelta
from werkzeug import urls

from odoo import _, fields, models
from odoo.exceptions import UserError, ValidationError

# from odoo.addons.payment_paypal import const
# from odoo.addons.payment_paypal.controllers.main import PaypalController
from odoo import api, fields, models

class PaymentProvider(models.Model):
    _name= "payment.provider"


