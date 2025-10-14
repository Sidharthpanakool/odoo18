# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
from email.policy import default
from odoo import api, fields, models, Command
from odoo.api import readonly


class ResPartner(models.Model):
    _inherit = "res.partner"

    products=fields.Many2many('product.product','products')

    def action_recalculate_button(self):
        product_list=[]
        product_qty = self.env['ir.config_parameter'].sudo().get_param('s_o_from_customer.minimum_product_limit')
        order_lines=self.sale_order_ids.mapped('order_line').filtered(lambda p: p.product_uom_qty >= float(product_qty))
        product_list.append(order_lines.product_id.id)
        print(product_list)
        self.products = product_list

    def action_create_so(self):
        self.env['sale.order'].create({
            'partner_id': self.id,
            'order_line': [
                Command.create({
                    'product_id': rec})
                for rec in self.products.ids
            ],
        })



