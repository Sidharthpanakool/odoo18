# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
from email.policy import default
from odoo import api, fields, models, Command
from odoo.api import readonly


class ResPartner(models.Model):
    _inherit = "res.partner"

    products=fields.Many2many('product.product','products')

    def action_recalculate_button(self):
        product_qty = self.env['ir.config_parameter'].sudo().get_param('s_o_from_customer.minimum_product_limit')
        print(product_qty)
        # sale_order = self.sale_order_ids
        # print('sale_order',sale_order)
        sale_order_lines = self.sale_order_ids.mapped('order_line.product_uom_qty')
        order_line_products=self.sale_order_ids.mapped('order_line.product_template_id')
        print(sale_order_lines)
        print(order_line_products)

        for rec in sale_order_lines:
            if rec< float(product_qty):
                # print(rec)
                print("Hiii")
                # print(self.sale_order_ids.order_line.product_template_id)

                # product_list.append(self.sale_order_ids.product_id.id)




        # product_list=[]

        # for rec in sale_order:
        #     if rec.total_product_qty>= float(product_qty):
        #         sale_order_line=self.env['sale.order.line'].search([('order_id','=',rec.id)])
        #         print(sale_order_line)
        #         for rec in sale_order_line:
        #
        #             product_list.append(rec.product_id.id)
        #             print('list',product_list)
        # self.products=product_list


    def action_create_so(self):
        print(self.products.ids)


        # for rec in self.products.ids:
        #     print(rec)
        #
        # sale_order = self.env['sale.order'].create({
        #     'partner_id': self.id,
        #     'order_line': [
        #         Command.create({
        #             'product_id': rec})
        #         for rec in self.products.ids
        #     ],
        # })
        # print(sale_order)

