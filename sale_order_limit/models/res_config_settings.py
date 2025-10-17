from ast import literal_eval
from email.policy import default

from odoo import api, fields, models


class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    amount_limit = fields.Float(string='Amount Limit', config_parameter='task.amount_limit', help='Set Amount Limit',
                                default=50000)



