# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models

class ConsumedParts(models.Model):
    _name = "consumed.parts"
    _description = "Consumed Parts"

    product_id = fields.Many2one(
        comodel_name='product.template',
        string="Product")

    product_uom_qty = fields.Float(string="Quantity", default=1)
    currency_id = fields.Many2one(related='product_id.currency_id')
    list_price = fields.Float(related='product_id.list_price')
    total_price = fields.Float(string="Total", compute='_compute_total_price')

    consumed_product_id = fields.Many2one('vehicle.repair',
                                          'Consumed products id')

    @api.depends( 'list_price', 'product_uom_qty')
    def _compute_total_price(self):
        """For calculating consumed parts price by multiplying price and product quantity"""
        for record in self:
            record.total_price = record.list_price * record.product_uom_qty
