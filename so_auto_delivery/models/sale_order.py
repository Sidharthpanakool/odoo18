# Part of Odoo. See LICENSE file for full copyright and licensing details.
from odoo import fields, models,api
from odoo.exceptions import ValidationError

class SaleOrder(models.Model):
    _inherit = "sale.order"

    def action_confirm(self):
        product = self.env['product.product'].search([('default_code','=','Delivery_010')],limit=1)
        if self.amount_untaxed < 1500:
            self.order_line.create({
                'order_id': self.id,
                'product_id': product.id,
                'product_uom_qty': 1,
                'price_unit': 99,
            })
        return super().action_confirm()
