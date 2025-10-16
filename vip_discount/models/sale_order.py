# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
from odoo import api, models


class SaleOrder(models.Model):
    _inherit = "sale.order"

    @api.onchange('partner_id')
    def _check_vip_discount(self):
        for line in self.order_line:
            if self.partner_id.is_vip:
                line.discount = self.partner_id.vip_discount
            else:
                line.discount = 0.0




