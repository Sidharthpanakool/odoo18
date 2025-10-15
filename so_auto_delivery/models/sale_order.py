# Part of Odoo. See LICENSE file for full copyright and licensing details.
from odoo import  models
from odoo.exceptions import ValidationError

class SaleOrder(models.Model):
    _inherit = "sale.order"

    def action_confirm(self):
        delivery_product = self.env.ref('product.product_product_local_delivery')
        if self.amount_untaxed < 1500:
            self.order_line.create({
                'order_id': self.id,
                'product_id': delivery_product.id,
                'product_uom_qty': 1,
                'price_unit': 99,
            })
        return super().action_confirm()
