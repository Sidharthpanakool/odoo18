from ast import literal_eval
from email.policy import default

from odoo import api, fields, models
class ResConfigSettings(models.TransientModel):
    """Extension of 'res.config.settings' for configuring delivery settings."""
    _inherit = 'res.config.settings'

    storage_location=fields.Many2one("stock.location",string="Storage location",config_parameter='pos_storage_location.enable_storage_location')

    enable_storage_location=fields.Boolean(string="Enable Storage location",config_parameter='pos_storage_location.storage_location')



