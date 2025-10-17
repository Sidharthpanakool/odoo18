# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
from odoo import  models


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    def action_confirm(self):
        lines = self.order_line.filtered(lambda o: o.margin_percent < o.product_id.categ_id.minimum_margin_percent)
        for line in lines:
            if not self.env.user.has_group('sales_team.group_sale_manager') and line:
                self.message_post(body = f"In SO{self.id}, Product {line.product_id.name} has margin percentage "
                                         f"{line.margin_percent * 100} is less than "
                                         f"{line.product_id.categ_id.minimum_margin_percent * 100}.")

                self.env['bus.bus']._sendone(self.env.user.partner_id, 'simple_notification', {
                    'type': 'danger',
                    'title': ("Warning"),
                    'message': (f'Product {line.product_id.name} has margin {line.margin_percent * 100} is lower '
                                f'than minimum margin percentage {line.product_id.categ_id.minimum_margin_percent * 100}.')
                })
            else:
                return super().action_confirm()
