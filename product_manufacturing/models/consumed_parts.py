from odoo import fields, models

class ConsumedParts(models.Model):
    _name = "consumed.parts"
    _description = "Consumed Parts"

    product_id = fields.Many2one(comodel_name='product.template', string="Product", required=True)

    product_uom_qty = fields.Float(string="Quantity", default=1)

    consumed_product_id = fields.Many2one('product.assembly',
                                          'Consumed products id')

    # stock_location = fields.



#
#         bom_id = fields.Many2one('product.bom', string="BoM Reference", ondelete='cascade')
#         product_id = fields.Many2one('product.product', string="Component", required=True)
#         quantity = fields.Float(string="Quantity", required=True, default=1.0)

