from odoo import models, fields, api, Command
from odoo.exceptions import UserError


class ProductCreation(models.Model):
    _name = "product.creation"
    _description = "Product Creation Order"
    _rec_name = "product_id"

    product_id = fields.Many2one('product.product', string="Product to Produce", required=True)
    bom_id = fields.Many2one('product.bom', string="BoM")
    quantity = fields.Float(string="Quantity to Produce", default=1)
    state = fields.Selection([('draft','Draft'),('done','Done')], default='draft')
    location_id = fields.Many2one('stock.location', string="Stock Location", required=True)
    component_line_ids = fields.One2many('product.creation.component.line', 'creation_id', string="Components")


    @api.onchange('product_id')
    def _onchange_product_id(self):
        for rec in self:
            rec.component_line_ids.unlink()
            if rec.product_id:
                bom = self.env['product.bom'].search([('product_id','=',rec.product_id.id)],order='id asc',limit=1)
                rec.bom_id = bom or False
                if bom:
                    lines = []
                    for line in bom.bom_line_ids:
                        lines.append(Command.create({
                            'product_id': line.product_id.id,
                            'quantity': line.product_uom_qty * rec.quantity,
                        }))
                    rec.component_line_ids = lines

    @api.onchange('quantity')
    def _onchange_quantity(self):
        for rec in self:
            for line in rec.component_line_ids:
                if rec.bom_id:
                    bom_line = rec.bom_id.bom_line_ids.filtered(
                        lambda l: l.product_id == line.product_id
                    )
                    if bom_line:
                        line.quantity = bom_line.product_uom_qty * rec.quantity

    def action_produce(self):
        StockQuant = self.env['stock.quant']
        for rec in self:
            if rec.state == 'done':
                raise UserError("This order is already done.")
            if not rec.component_line_ids:
                raise UserError("No components to consume.")

            for line in rec.component_line_ids:
                qty_needed = rec.component_line_ids.quantity * rec.quantity

                for quant in StockQuant.search([('product_id', '=', line.product_id.id), ('location_id', '=', rec.location_id.id)],order='quantity desc'):
                    if quant.available_quantity < qty_needed:
                        raise UserError(
                            f"Not enough stock for component {line.product_id.name}."
                        )
                    else:
                        quant.write({'quantity': quant.quantity - line.quantity})

            quant = StockQuant.search(
                [('product_id', '=', rec.product_id.id), ('location_id', '=', rec.location_id.id)], limit=1)
            if quant:
                quant.write({'quantity': quant.quantity + rec.quantity})
            else:
                StockQuant.create([{
                    'product_id': rec.product_id.id,
                    'location_id': rec.location_id.id,
                    'quantity': rec.quantity
                }])
            rec.state = 'done'





    # @api.onchange('bom_id')
    # def _onchange_bom_id(self):
    #     print("Hiii")
    #     for rec in self:
    #         # rec.component_line_ids.unlink()
    #         print(rec)
    #         if rec.bom_id:
    #             print(rec.id)
                # bom_ids = self.env['product.bom'].search([('product_id','=',rec.product_id.id)])
                # print(bom_ids)
                # for bom in bom_ids:
                #     if bom:
                #         lines = []
                #         for line in bom.bom_line_ids:
                #             lines.append(Command.create({
                #                 'product_id': line.product_id.id,
                #                 'quantity': line.product_uom_qty * rec.quantity,
                #
                #             }))
                #         rec.component_line_ids = lines

        # for rec in self:
        #     rec.component_line_ids.unlink()
        #     if rec.product_id:
        #         bom = self.env['product.bom'].search([('product_id','=',rec.product_id.id)])
        #         rec.bom_id = bom or False
        #         if bom:
        #             lines = []
        #             for line in bom.bom_line_ids:
        #                 lines.append(Command.create({
        #                     'product_id': line.product_id.id,
        #                     'quantity': line.product_uom_qty * rec.quantity,
        #                 }))
        #             rec.component_line_ids = lines






            # StockPicking = self.env['stock.picking']
            # stock_location = self.env.ref('stock.stock_location_stock')
            # production_location = self.env.ref('stock.stock_location_stock')


            # moves = []
            #
            # for line in rec.component_line_ids:
            #     moves.append(Command.create({
            #         'name': line.product_id.name,
            #         'product_id': line.product_id.id,
            #         'product_uom_qty': line.quantity,
            #         'product_uom': line.product_id.uom_id.id,
            #         'location_id': stock_location.id,
            #         'location_dest_id': production_location.id,
            #     }))
            #
            # moves.append(Command.create({
            #     'name': rec.product_id.name,
            #     'product_id': rec.product_id.id,
            #     'product_uom_qty': rec.quantity,
            #     'product_uom': rec.product_id.uom_id.id,
            #     'location_id': production_location.id,
            #     'location_dest_id': stock_location.id,
            # }))
            #
            # picking = StockPicking.create([{
            #     'picking_type_id': self.env.ref('stock.picking_type_internal').id,
            #     'location_id': stock_location.id,
            #     'location_dest_id': stock_location.id,
            #     'move_ids_without_package': moves,
            # }])
            #
            # picking.action_confirm()
            # picking.action_assign()
            # picking._action_done()








    # def action_create_pmo(self):
    #     StockQuant = self.env['stock.quant']
    #     print("Hiiii")
    #
    #     for record in self:
    #     #     if record.state == 'done':
    #     #         raise UserError("This product creation has already been processed.")
    #
    #         for component in record.components_ids:
    #             required_qty = component.product_uom_qty * record.quantity
    #
    #             available_qty = sum(StockQuant.search(
    #                 [('product_id', '=', component.product_id.id), ('location_id', '=', record.location_id.id)]).mapped(
    #                 'quantity'))
    #
    #             if available_qty < required_qty:
    #                 raise UserError(f"Not enough stock for {component.product_id.name} in {record.location_id.name}")
    #
                # remaining_qty = required_qty
                # for quant in StockQuant.search(
                #         [('product_id', '=', component.product_id.id), ('location_id', '=', record.location_id.id)],
                #         order='quantity desc'):
                #     if quant.quantity >= remaining_qty:
                #         quant.sudo().write({'quantity': quant.quantity - remaining_qty})
                #         remaining_qty = 0
                #         break
                #     else:
                #         remaining_qty -= quant.quantity
                #         quant.sudo().write({'quantity': 0})
    #
            # quant = StockQuant.search(
            #     [('product_id', '=', record.product_id.id), ('location_id', '=', record.location_id.id)], limit=1)
            # if quant:
            #     quant.sudo().write({'quantity': quant.quantity + record.quantity})
            # else:
            #     StockQuant.create([{
            #         'product_id': record.product_id.id,
            #         'location_id': record.location_id.id,
            #         'quantity': record.quantity
            #     }])
    #
    #         record.state = 'done'






    # @api.depends('bom_id', 'product_id')
    # def _compute_uom_id(self):
    #     for production in self:
    #         if production.state != 'draft':
    #             continue
    #         if production.bom_id and production._origin.bom_id != production.bom_id:
    #             production.product_uom_id = production.bom_id.product_uom_id
    #         elif production.product_id:
    #             production.product_uom_id = production.product_id.uom_id
    #         else:
    #             production.product_uom_id = False
    #
    # product_uom_id = fields.Many2one(
    #     'uom.uom', 'Product Unit of Measure',
    #     readonly=False, required=True, compute='_compute_uom_id', store=True, copy=True, precompute=True,
    #     domain="[('category_id', '=', product_uom_category_id)]")