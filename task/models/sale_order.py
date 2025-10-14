# Part of Odoo. See LICENSE file for full copyright and licensing details.
from odoo import fields, models,api
from odoo.exceptions import ValidationError

class SaleOrder(models.Model):
    _inherit = "sale.order"

    total_product_qty = fields.Float(
        string='Total Product Quantity',
        compute='_compute_total_product_qty',
        store=True
    )

    def action_confirm(self):
        delivery_product=self.env.ref('task.delivery_product_99')
        product=self.env['product.product'].search([('product_tmpl_id','=',delivery_product.id)],limit=1)
        sale_order_line=self.env['sale.order.line'].search([('order_id','=',self.id)])
        if self.amount_untaxed<1500:
            sale_order_line.create({
                'order_id':self.id,
                'product_id': product.id,
                'name': delivery_product.name,
                'product_uom_qty':1,
                'price_unit':delivery_product.list_price,
                'price_tax': delivery_product.taxes_id,

            })
        return super().action_confirm()















    # def action_confirm(self):
    #     product_qty=self.env['ir.config_parameter'].sudo().get_param('task.minimum_product_limit')
    #     sale_order_line_qty=self.env['sale.order.line'].search([('order_id','=',self.id)])
    #     total_qty=sum(rec.product_uom_qty for rec in sale_order_line_qty)
    #     print(total_qty)
    #     if total_qty> float(product_qty):
    #         print(product_qty)
    #     return super().action_confirm()





    @api.depends('order_line.product_uom_qty')
    def _compute_total_product_qty(self):
        for order in self:
            order.total_product_qty = sum(line.product_uom_qty for line in order.order_line)













        # def action_confirm(self):
        #
        #     if not self.env.user.has_group('sales_team.group_sale_manager') and self.amount_total > float(self.env['ir.config_parameter'].sudo().get_param('task.amount_limit')):
        #         raise ValidationError(_('your limit exceeded'))
        #     return super().action_confirm()

















    # def _compute_customer_limit(self):
    #     amount=self.env['ir.config_parameter'].sudo().get_param(
    #             'res.config.settings.storage_location')
    #
    #     print('amount',amount)

















    # # -*- coding: utf-8 -*-
    # # Part of Odoo. See LICENSE file for full copyright and licensing details.
    # from odoo import Command, api, fields, models
    # from odoo.exceptions import UserError
    # from odoo import api, models, fields
    # from ast import literal_eval
    # from odoo.tools import groupby
    #
    # class ProductProduct(models.Model):
    #     _inherit = 'product.product'
    #
    #     product_qty = fields.Float(string="Product Qty", required=True, compute="_compute_product_qty", store=False)
    #
    #     def _compute_product_qty(self):
    #
    #         location_in_settings = self.env['ir.config_parameter'].sudo().get_param(
    #             'res.config.settings.storage_location')
    #         print("location_in_settings", location_in_settings)
    #
    #         stock = self.env['stock.quant'].search([])
    #         stock = list(stock.location_id)
    #         print("stock.location_id", stock)
    #         pos_config = self.env['product.product'].search([])
    #         location_ids = pos_config if pos_config else False
    #
    #         for product in self:
    #             qty = 0
    #             if location_ids:
    #                 quants = self.env["stock.quant"].search([('product_id', '=', product.id)]).read()
    #                 print('quants', quants)
    #                 if quants:
    #                     qty = quants[0]['quantity']
    #             product.product_qty = qty
    #             print("PPPPPPPPP", product.product_qty)
    #
    #     @api.model
    #     def _load_pos_data_fields(self, config_id):
    #         params = super()._load_pos_data_fields(config_id)
    #         params += ['product_qty']
    #         return params
