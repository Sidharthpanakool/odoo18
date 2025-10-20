from odoo import fields, models

class ConsumedParts(models.Model):
    _name = "consumed.parts"
    _description = "Consumed Parts"

    product_id = fields.Many2one(
        comodel_name='product.template',
        string="Product")

    product_uom_qty = fields.Float(string="Quantity", default=1)

    consumed_product_id = fields.Many2one('product.assembly',
                                          'Consumed products id')