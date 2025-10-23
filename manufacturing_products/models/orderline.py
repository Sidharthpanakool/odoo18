from odoo import fields, models ,api


class OrderLine(models.Model):
    _name = "order.line"

    product_id = fields.Many2one(comodel_name='product.product', string="Product", required=True, )
    product_uom_qty = fields.Float(string="Quantity", default=1)
    product_bom_id = fields.Many2one("product.bom", "Components")


