# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
from odoo import Command, api, fields, models
from odoo.exceptions import UserError
from odoo import api,models,fields
from ast import literal_eval
from odoo.tools import groupby


class ProductProduct(models.Model):
    _inherit = 'product.product'

    product_qty=fields.Float(string="Product Qty",required=True,compute="_compute_product_qty",store=False)

    def _compute_product_qty(self):

        location_in_settings=self.env['ir.config_parameter'].sudo().get_param('res.config.settings.storage_location')
        print("location_in_settings",location_in_settings)

        stock=self.env['stock.quant'].search([])
        stock=list(stock.location_id)
        print("stock.location_id",stock)
        pos_config = self.env['product.product'].search([])
        location_ids = pos_config if pos_config else False

        for product in self:
            qty = 0
            if location_ids:
                quants = self.env["stock.quant"].search([('product_id', '=',product.id)]).read()
                print('quants', quants)
                if quants:
                    qty = quants[0]['quantity']
            product.product_qty = qty
            print("PPPPPPPPP", product.product_qty)

    @api.model
    def _load_pos_data_fields(self, config_id):
        params = super()._load_pos_data_fields(config_id)
        params += ['product_qty']
        return params
