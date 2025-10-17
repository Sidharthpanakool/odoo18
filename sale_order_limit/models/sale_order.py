# Part of Odoo. See LICENSE file for full copyright and licensing details.
from odoo import fields, models, api
from odoo.exceptions import ValidationError


class SaleOrder(models.Model):
    _inherit = "sale.order"

    def action_confirm(self):
        if not self.env.user.has_group('sales_team.group_sale_manager') and self.amount_total > float(
                self.env['ir.config_parameter'].sudo().get_param('task.amount_limit')):
            raise ValidationError('your limit exceeded')
        return super().action_confirm()