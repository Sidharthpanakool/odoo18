from odoo import models, fields

class ProductCreationComponentLine(models.Model):
    _name = "product.creation.component.line"
    _description = "Components for Product Creation"


    creation_id = fields.Many2one('product.creation', string="Creation Order", ondelete='cascade')
    product_id = fields.Many2one('product.product', string="Component", required=True)
    quantity = fields.Float(string="Quantity", default=1)