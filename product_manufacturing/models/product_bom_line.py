from odoo import api, fields, models, exceptions

class ProductBomLine(models.Model):
    _name = "product.bom.line"
    _description = "BoM Component Line"

    product_bom_id = fields.Many2one('product.bom', string="BoM")
    product_id = fields.Many2one('product.product', string="Component", required=True)
    product_uom_qty = fields.Float(string="Quantity", default=1)
