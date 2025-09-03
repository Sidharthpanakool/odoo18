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
    #
    #     print("icp",icp_sudo)
    #
    #     enable_storage_location = icp_sudo.get_param('res.config.settings.enable_storage_location')
    #     storage_location = icp_sudo.get_param('res.config.settings.storage_location')
    #
    #     print("Sto",storage_location)
    #
    #     res.update(
    #         enable_storage_location=enable_storage_location,
    #         storage_location=fields.Command.set(storage_location) if storage_location else False
    #     )
    #     return res
    #
    # def set_values(self):
    #     """Set the values. The new values are stored in the configuration parameters."""
    #     res = super(ResConfigSettings, self).set_values()
    #     self.env['ir.config_parameter'].sudo().set_param(
    #         'res.config.settings.enable_storage_location', self.enable_storage_location)
    #     self.env['ir.config_parameter'].sudo().set_param(
    #         'res.config.settings.storage_location',self.storage_location.ids)
    #     return res









    # def get_values(self):
    #     """Get the values from settings."""
    #     res = super(ResConfigSettings, self).get_values()
    #     icp_sudo = self.env['ir.config_parameter'].sudo()
    #     enable_storage_location = icp_sudo.get_param('res.config.settings.enable_storage_location')
    #     storage_location = icp_sudo.get_param('res.config.settings.storage_location')
    #     res.update(
    #         enable_storage_location=enable_storage_location,
    #         storage_location=[(6, 0, literal_eval(storage_location))] if storage_location else False,
    #     )
    #     return res
    #
    # def set_values(self):
    #     """Set the values. The new values are stored in the configuration parameters."""
    #     res = super(ResConfigSettings, self).set_values()
    #     self.env['ir.config_parameter'].sudo().set_param(
    #         'res.config.settings.enable_storage_location', self.enable_storage_location)
    #     self.env['ir.config_parameter'].sudo().set_param(
    #         'res.config.settings.storage_location',
    #         self.storage_location.ids)
    #     return res

    # @api.model
    # def get_values(self):
    #     res = super(ResConfigSettings, self).get_values()
    #     expense_alias = self.env.ref('hr_expense.mail_alias_expense', raise_if_not_found=False)
    #     res.update(
    #         hr_expense_alias_prefix=expense_alias.alias_name if expense_alias else False,
    #         hr_expense_alias_domain_id=expense_alias.alias_domain_id if expense_alias else False,
    #     )
    #     return res
    #
    # def set_values(self):
    #     super().set_values()
    #     expense_alias = self.env.ref('hr_expense.mail_alias_expense', raise_if_not_found=False)
    #     if not expense_alias and self.hr_expense_alias_prefix:
    #         # create data again
    #         alias = self.env['mail.alias'].sudo().create({
    #             'alias_contact': 'employees',
    #             'alias_domain_id': self.env.company.alias_domain_id.id,
    #             'alias_model_id': self.env['ir.model']._get_id('hr.expense'),
    #             'alias_name': self.hr_expense_alias_prefix,
    #         })
    #         self.env['ir.model.data'].sudo().create({
    #             'name': 'mail_alias_expense',
    #             'module': 'hr_expense',
    #             'model': 'mail.alias',
    #             'noupdate': True,
    #             'res_id': alias.id,
    #         })
    #     elif expense_alias and expense_alias.alias_name != self.hr_expense_alias_prefix:
    #         expense_alias.alias_name = self.hr_expense_alias_prefix

    # @api.model
    # def get_values(self):
    #     res = super(ResConfigSettings, self).get_values()
    #     icp_sudo = self.env['ir.config_parameter'].sudo()
    #     # res = super().get_values()
    #     # authorize = self.env.ref('payment.payment_provider_authorize').sudo()
    #     res['authorize_capture_method'] = 'manual' if icp_sudo.capture_manually else 'auto'
    #     return res
    #
    # def set_values(self):
    #     super().set_values()
    #     authorize = self.env.ref('payment.payment_provider_authorize').sudo()
    #     capture_manually = self.authorize_capture_method == 'manual'
    #     if authorize.capture_manually != capture_manually:
    #         authorize.capture_manually = capture_manually

    # @api.model
    # def get_values(self):
    #     res = super(ResConfigSettings, self).get_values()
    #     company = self.env.company
    #     res.update({
    #         'overtime_company_threshold': company.overtime_company_threshold,
    #         'overtime_employee_threshold': company.overtime_employee_threshold,
    #     })
    #     return res
    #
    # def set_values(self):
    #     super().set_values()
    #     company = self.env.company
    #     # Done this way to have all the values written at the same time,
    #     # to avoid recomputing the overtimes several times with
    #     # invalid company configurations
    #     fields_to_check = [
    #         'overtime_company_threshold',
    #         'overtime_employee_threshold',
    #     ]
    #     if any(self[field] != company[field] for field in fields_to_check):
    #         company.write({field: self[field] for field in fields_to_check})
