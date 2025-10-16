# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models


class SaleOrderLine(models.Model):
    _inherit = "sale.order.line"

    @api.onchange('product_template_id')
    def _check_customer_add_discount(self):
        for line in self:
            if line.order_partner_id.is_vip:
                line.discount = self.order_partner_id.vip_discount
            else:
                line.discount = 0.0


