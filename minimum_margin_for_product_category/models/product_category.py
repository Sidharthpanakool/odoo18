from odoo import models, fields

class ProductCategory(models.Model):
    _inherit = "product.category"

    minimum_margin_percent = fields.Float(string = "Minimum Margin Percentage", default = .15)