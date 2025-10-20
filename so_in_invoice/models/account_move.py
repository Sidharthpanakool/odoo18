# Part of Odoo. See LICENSE file for full copyright and licensing details.
from odoo import api, models, fields, Command


class AccountMove(models.Model):
    _inherit = "account.move"


    related_sale_orders_ids = fields.Many2many(comodel_name='sale.order',
                                               string ="Related SaleOrders",
                                               domain="[('state', '=', 'sale'),('invoice_status','!=','invoiced'),('partner_id','=',partner_id)]"
                                               )

    @api.onchange('related_sale_orders_ids')
    def _order_line(self):
        order_line_list = []
        for rec in self.related_sale_orders_ids.mapped('order_line'):

            order_line_list.append(Command.create({
                'product_id': rec.product_id.id,
                'quantity': rec.product_uom_qty,
                'price_unit': rec.price_unit,
                'price_subtotal': rec.price_subtotal,
                'sale_line_ids': [(6, 0, [rec.id])],
            }))
            print(rec.id)
        self.invoice_line_ids =  order_line_list
        print(self.invoice_line_ids)





            # sale_ids = self.partner_id.mapped('sale_order_ids').filtered(lambda o: o.state == 'sale'
            #                                                    and not o.invoice_status=='invoiced' and o.partner_id == self.partner_id)
            # print(sale_ids)





            # print('sa', sale_ids)
            # existing_sale_ids = self.related_sale_orders_ids
            # if not existing_sale_ids:
            #     existing_sale_ids += sale_ids
            # print(self.related_sale_orders_ids)
            # print(sale_ids)
            # sale_ids = self.env['sale.order'].search([('invoice_status','!=','invoiced'),('partner_id','=',self.partner_id.id),('state','=','sale')])
