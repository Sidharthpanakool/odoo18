from email.policy import default

from odoo import fields,models,api

class ProductCreation(models.Model):
    _name = "product.creation"
    _rec_name = 'assembly_id'

    product_assembly_id = fields.Many2one('product.assembly', string="Select Assembly Product")
    product_id = fields.Many2one(related='product_assembly_id.product_id', string="Product")

    components_ids = fields.One2many(related='product_assembly_id.consumed_parts_ids')
    quantity = fields.Float(string="Quantity", default=1.0)


    state = fields.Selection([
        ('draft', 'Draft'),
        ('done', 'Done')
    ], default='draft')

    assembly_id = fields.Char(string="Order id", required=True, readonly=True, default='New', copy=False, tracking=True)

    @api.model
    def create(self, vals):
        if vals.get('assembly_id', 'New') == 'New':
            vals['assembly_id'] = self.env['ir.sequence'].next_by_code('product.creation.code') or 'New'
        return super(ProductCreation, self).create(vals)



    @api.onchange('quantity')
    def _onchange_product(self):
        print("Hiiii")
        print(self.quantity)
        # if self.quantity:
        for record in self.components_ids:
            record.product_uom_qty = record.product_uom_qty * self.quantity

    # @api.depends('quantity','self.components_ids.product_uom_qty')
    # def _compute_product_uom_quantity(self):




    def action_create_pmo(self):
        print("action_create_pmo")














#     class ProductCreation(models.Model):
#         _name = 'product.creation'
#         _description = 'Product Creation'
#
#         name = fields.Char(string="Reference", required=True, default='New')
#         bom_id = fields.Many2one('product.bom', string="Select BoM", required=True)
#         product_id = fields.Many2one(related='bom_id.product_id', string="Product to Create", store=True)
#         quantity = fields.Float(string="Quantity to Produce", required=True, default=1.0)
#         state = fields.Selection([
#             ('draft', 'Draft'),
#             ('done', 'Done')
#         ], default='draft')
#
#         @api.model
#         def create(self, vals):
#             if vals.get('name', 'New') == 'New':
#                 vals['name'] = self.env['ir.sequence'].next_by_code('product.creation') or 'New'
#             return super(ProductCreation, self).create(vals)
#
#         def action_confirm_creation(self):
#             for rec in self:
#                 if rec.state == 'done':
#                     raise UserError("This production is already done.")
#                 bom = rec.bom_id
#                 if not bom.component_line_ids:
#                     raise UserError("No components defined in the selected BoM.")
#
#                 # Decrease component quantities
#                 for line in bom.component_line_ids:
#                     component = line.product_id
#                     consume_qty = line.quantity * rec.quantity
#                     if component.qty_available < consume_qty:
#                         raise UserError(f"Not enough {component.display_name} in stock to produce.")
#
#                     # Adjust stock using quants
#                     quant = self.env['stock.quant'].search([
#                         ('product_id', '=', component.id),
#                         ('location_id.usage', '=', 'internal')
#                     ], limit=1)
#                     if quant:
#                         quant.quantity -= consume_qty
#                     else:
#                         raise UserError(f"No stock quant found for {component.display_name}.")
#
#                 finished_quant = self.env['stock.quant'].search([
#                     ('product_id', '=', rec.product_id.id),
#                     ('location_id.usage', '=', 'internal')
#                 ], limit=1)
#
#                 if finished_quant:
#                     finished_quant.quantity += rec.quantity
#                 else:
#                     location = self.env.ref('stock.stock_location_stock')
#                     self.env['stock.quant'].create({
#                         'product_id': rec.product_id.id,
#                         'location_id': location.id,
#                         'quantity': rec.quantity,
#                     })
#
                # rec.state = 'done'