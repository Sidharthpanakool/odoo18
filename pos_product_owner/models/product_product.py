# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
from odoo import Command, api, fields, models
from odoo.exceptions import UserError


# class PosOrder(models.Model):
#     _inherit = 'pos.order'
#
#     @api.model
#     def _order_fields(self, ui_order):
#         res = super()._order_fields(ui_order)
#         res['product_owner_id'] = ui_order.get('product_owner_id')
#         return res
#         print("hdhdhdhdhdhd")

class ProductProduct(models.Model):
    _inherit = 'product.product'

    @api.model
    def _load_pos_data_fields(self, config_id):
        params = super()._load_pos_data_fields(config_id)
        params += ['product_owner_id']
        return params
