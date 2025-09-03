# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
from odoo import Command, api, fields, models
from odoo.exceptions import UserError
from odoo import api,models,fields

class ProductProduct(models.Model):
    # _inherit = 'product.product'
    _inherit = 'pos.session'

    product_qty=fields.Float(string="Product Qty",required=True)

    # ,compute="_compute_product_qty"

    @api.model
    def _load_pos_data_fields(self, config_id):
        params = super()._load_pos_data_fields(config_id)
        params += ['product_qty']
        return params


    # def _compute_product_qty(self):
    #     location_in_settings=self.env['res.config.settings'].search([])
    #     product_id=self.env['product.product'].search([])
    #     stock=self.env['stock.quant'].search([])
    #     product_temp=self.env['product.template'].search([])
    #
    #     for i in product_id:
    #         print("product.product.id",i.id)
    #
    #     for rec in product_temp:
    #         print("prod temp.name:",rec.name)
    #
    #     for abc in stock:
    #         print("stock qty",abc.quantity)
    #         print("Stock location id",abc.location_id)
    #
    #     print("settings location",location_in_settings.storage_location)
    #
    #     product_qty = 0
    #     for record in self:
    #         # print("qty", record.qty_available)
    #         print("product_qty", record.product_qty)
    #
    #     if location_in_settings.storage_location == stock.location_id and record.id == stock.product_id:
    #         product_qty = stock.quantity
    #         print("product_qty_product_qty",product_qty)










        # query = """
        #          SELECT
        #             pr.default_code,
        #             pr.id,
        #             tem.name,
        #             stock_quant.location_id,
        #             set.storage_location,
        #             stock_quant.quantity,
        #             pr.product_qty
        #             from stock_quant
        #             left join res_config_settings as set on stock_quant.location_id=set.storage_location
        #             left join product_product as pr on stock_quant.product_id=pr.id
        #             left join product_template as tem on pr.product_tmpl_id=tem.id
        #             order by pr.id
        #         """




    # def _compute_product_qty(self,params):
    #     products=super()._compute_product_qty(params)
    #     picking_type=self.config.id.picking_type_id
    #     location_id=picking_type.default_location_src_id.id
    #     for product in products:
    #         pp=self.env['product.product'].browse([product.get('id')])
    #         product_qty=pp.with_context(location=location_id)._compute_quantities_dict(None,None,None,None,None)
    #         for pos_product in product_qty:
    #             product['pos_qty_available']=product_qty.get(pos_product).get('qty_available')
    #         return products



