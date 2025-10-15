from odoo import models,fields

class ProductCreationRequest(models.Model):
    _name = "product.creation.request"

    name = fields.Char(string="Name")
    product_name = fields.Char(string='Product Name')
    sales_price = fields.Float(string="Sales Price")
    cost_price = fields.Float(string="Cost Price")
    default_code = fields.Char(string="Default code")
    list_price = fields.Float(string="List price")
