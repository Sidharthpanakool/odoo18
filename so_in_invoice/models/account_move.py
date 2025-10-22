# Part of Odoo. See LICENSE file for full copyright and licensing details.
from odoo import api, models, fields, Command


class AccountMove(models.Model):
    _inherit = "account.move"

    related_sale_orders_ids = fields.Many2many(comodel_name='sale.order',
                                               string ="Related SaleOrders",
                                               domain="[('state', '=', 'sale'),('invoice_status','!=','invoiced'),('partner_id','=',partner_id)]"
                                               )

    @api.onchange('related_sale_orders_ids')
    def _onchange_order_line(self):
        merged_lines = {}
        for rec in self.related_sale_orders_ids.mapped('order_line'):
            key = (rec.product_id.id, rec.price_unit)
            if key in merged_lines:
                merged_lines[key]['quantity'] += rec.product_uom_qty
            else:
                merged_lines[key] = {
                    'product_id': rec.product_id.id,
                    'quantity': rec.product_uom_qty,
                    'price_unit': rec.price_unit,
                }
        self.invoice_line_ids = [Command.clear()]
        self.invoice_line_ids = [Command.create(vals) for vals in merged_lines.values()]







        # for vals in merged_lines.values():
        #     order_line_list.append(fields.Command.create(vals))
        # groups = super().create([self._sanitize_vals(vals) for vals in vals_list])

        # order_line_list.append(fields.Command.create(vals) for vals in merged_lines.values())

        # @api.onchange('related_sale_orders_ids')
        # def _order_line(self):
        #     order_line_list = []
        #     self.invoice_line_ids = [Command.clear()]
        #     merged_lines = {}
        #
        #     for rec in self.related_sale_orders_ids.order_line:
        #         record=fields.Command.create({
        #             'product_id': rec.product_id.id,
        #             'quantity': rec.product_uom_qty,
        #             'price_unit': rec.price_unit,
        #             'price_subtotal': rec.price_subtotal,
        #             })
        #         print(record)
        #         order_line_list.append(record)
        #     self.invoice_line_ids = order_line_list




        # existing_record_line = self.invoice_line_ids.filtered(lambda o: o.product_id == record.product_id and o.price_unit == record.price_unit)
        # print('exist line id', existing_record_line)

        #
        # if existing_line:
        #     existing_line.product_qty += self.quantity
        #     existing_line.price_unit = self.price
        # print(order_line_list)


        # existing_inv = self.env['account.move'].search(
        #     [('state', '=', 'draft')], limit=1)

        # if existing_po:
        #     po = existing_po
        # else:
        #     po = self.env['purchase.order'].create([{
        #         'partner_id': top_vendor.id,
        #         'date_order': fields.Datetime.now(),
        #     }])


        # @api.onchange('related_sale_orders_ids')
        # def _order_line(self):
        #     order_line_list = []
        #     self.invoice_line_ids = [Command.clear()]
        #     merged_lines = {}
        #
        #     for rec in self.related_sale_orders_ids.order_line:
        #         order_line_list.append(fields.Command.create({
        #             'product_id': rec.product_id.id,
        #             'quantity': rec.product_uom_qty,
        #             'price_unit': rec.price_unit,
        #             'price_subtotal': rec.price_subtotal,
        #         })
        #         )
        #     self.invoice_line_ids = order_line_list
        #     print(order_line_list)

        # print(self.invoice_line_ids)
        #
        #     key = (rec.product_id.id, rec.price_unit)
        #     if key not in merged_lines:
        #         merged_lines[key] = {
        #             'product_id': rec.product_id.id,
        #             'quantity': rec.product_uom_qty,
        #             'price_unit': rec.price_unit,
        #
        #         }
        # print(self.invoice_line_ids)
        # i=0
        # for re in self.invoice_line_ids:
        #     # if re.product_id:
        #     #     print("hii")
        #     i+=1
        #     print(i)
        #     print(re.product_id)






    # @api.onchange('related_sale_orders_ids')
    # def _onchange_related_sale_orders_ids(self):
    #     self.invoice_line_ids = [Command.clear()]
    #     if not self.related_sale_orders_ids:
    #         return
    #
    #     merged_lines = {}
    #
    #     for rec in self.related_sale_orders_ids.mapped('order_line'):
    #         if rec.display_type:
    #             continue
    #
            # key = (rec.product_id.id, rec.price_unit)
            # if key not in merged_lines:
            #     merged_lines[key] = {
            #         'product_id': rec.product_id.id,
            #         'quantity': rec.product_uom_qty,
            #         'price_unit': rec.price_unit,
            #
            #     }
    #         else:
    #             merged_lines[key]['quantity'] += rec.product_uom_qty
    #             merged_lines[key]['sale_line_ids'][0][2].append(rec.id)
    #
    #     self.invoice_line_ids = [Command.create(vals) for vals in merged_lines.values()]


        # existing_product = self.invoice_line_ids.filtered(
        #     lambda o: o.product_id == rec.product_id and o.price_unit == rec.price_unit)
        # if existing_product:
        #     print("Existingggggggggggggggggggg")





        # result = {}
        # for d in self.invoice_line_ids:
        #     key = d['product_id'], d['price_unit']
        #     if key not in result:
        #         result[key] = {}
        #     result[key].update(d)

        # existing_product = self.invoice_line_ids.filtered(lambda o: o.product_id == rec.product_id and o.price_unit == rec.price_unit)
        # if existing_product:
        #     print("Existingggggggggggggggggggg")
        #     existing_product.quantity += rec.product_uom_qty
        #
        #     print(existing_product.quantity)
        #
        # existing_line = po.order_line.filtered(lambda o: o.product_id == product)
        #
        # print('exist line id', existing_line.id)

        # if existing_line:
        #     existing_line.product_qty += self.quantity
        #     existing_line.price_unit = self.price

        # print(existing_product)
        # print(rec)
        # print(rec.price_unit)

        # existing_product = self.invoice_line_ids.filtered(lambda o: o.product_id == rec.product_id and o.price_unit == rec.price_unit)
        # print(existing_product)
        # if existing_product:
        #     print(existing_product.quantity)
        #     print(order_line_list)
        #
        #     print("Hiiii")



        # existing_product_line = self.invoice_line_ids.filtered(lambda o: o.product_id == self.related_sale_orders_ids.order_line.product_id )
        # # and o.price_unit == self.related_sale_orders_ids.order_line.price_unit
        #
        # print(existing_product_line.id)











