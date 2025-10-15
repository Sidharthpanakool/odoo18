# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
from odoo import fields, models, Command


class ResPartner(models.Model):
    _inherit = "res.partner"

    products=fields.Many2many('product.product','products')

    def action_recalculate_button(self):
        product_qty = self.env['ir.config_parameter'].sudo().get_param('s_o_from_customer.minimum_product_limit')
        product_ids = self.sale_order_ids.mapped('order_line').filtered(lambda p: p.product_uom_qty >= float(product_qty)).mapped('product_id.id')
        self.products = product_ids

    def action_create_so(self):
        self.env['sale.order'].create([{
            'partner_id': self.id,
            'order_line': [
                Command.create({
                    'product_id': rec})
                for rec in self.products.ids
            ],
        }])



