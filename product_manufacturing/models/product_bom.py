from odoo import fields, models

class ProductBom(models.Model):
    _name = "product.bom"
    _description = "Bill of Materials"
    _rec_name = "product_id"

    # sequence = fields.Integer(string="Sequence", default=1)
    quantity = fields.Float(string="Quantity",default=1)
    product_id = fields.Many2one('product.product', string='Product', required=True)
    bom_line_ids = fields.One2many('product.bom.line', 'product_bom_id', string="Components")