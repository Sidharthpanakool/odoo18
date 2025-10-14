from ast import literal_eval
from email.policy import default

from odoo import api, fields, models
class ResConfigSettings(models.TransientModel):
    """Extension of 'res.config.settings' for configuring delivery settings."""
    _inherit = 'res.config.settings'



    minimum_product_limit = fields.Float('Minimum no: of product',config_parameter='s_o_from_customer.minimum_product_limit')

    #discount_limit = fields.Float(string='Limit amount',
    #                               config_parameter='sale_discount_limit.discount_limit',
    #                               help='The discount limit amount in percentage ')



