from odoo import fields,models

class ProductOwnerPos(models.Model):
    _inherit = "product.template"

    product_owner_id=fields.Many2one('res.partner',string="Product Owner")