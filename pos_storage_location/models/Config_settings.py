from ast import literal_eval
from odoo import api, fields, models
class ResConfigSettings(models.TransientModel):
    """Extension of 'res.config.settings' for configuring delivery settings."""
    _inherit = 'res.config.settings'

    enable_storage_location=fields.Boolean(string="Enable Storage location",config_parameter='pos_storage_location.enable_storage_location')

    storage_location=fields.Many2one("stock.location",string="Storage location",config_parameter='pos_storage_location.storage_location')

    # def get_values(self):
    #     """Get the values from settings."""
    #     res = super(ResConfigSettings, self).get_values()
    #     icp_sudo = self.env['ir.config_parameter'].sudo()
    #     print("icp",icp_sudo)
    #     enable_storage_location = icp_sudo.get_param('res.config.settings.enable_storage_location')
    #     storage_location = icp_sudo.get_param('res.config.settings.storage_location')
    #     print("Sto",storage_location)
    #     select_location_ids=icp_sudo.get_param('res.config.settings.select_location_ids')
    #     res.update(
    #         select_location_ids=select_location_ids,
    #         enable_storage_location=enable_storage_location,
    #         storage_location=fields.Command.set(storage_location) if storage_location else False
    #     )
    #     return res
    #
    #
    # def set_values(self):
    #     """Set the values. The new values are stored in the configuration parameters."""
    #     res = super(ResConfigSettings, self).set_values()
        # self.env['ir.config_parameter'].sudo().set_param(
        #     'res.config.settings.enable_storage_location', self.enable_storage_location)
        # self.env['ir.config_parameter'].sudo().set_param(
        #     'res.config.settings.storage_location',self.storage_location.ids)
    #     self.env['ir.config_parameter'].sudo().set_param(
    #         'res.config.settings.storage_location', self.select_location_ids.ids)
    #     return res

