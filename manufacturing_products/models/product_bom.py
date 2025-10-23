from odoo import fields, models ,api

class OrderLine(models.Model):
    _name = "product.bom"

    product_id = fields.Many2one('product.product',string='Product')
    quantity = fields.Float("Quantity")
    product_bom_ids = fields.One2many("order.line", "product_bom_id", "Product")