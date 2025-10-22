# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
from odoo import models,fields
from odoo.exceptions import UserError


class WizardProductProduct(models.TransientModel):
    _name = "wizard.product.product"
    _description = "Wizard product product"

    product_id = fields.Many2one('product.product', string="Product", required=True)
    quantity = fields.Float(string="Quantity", required=True, default=1)
    price = fields.Float(string="Unit Price", required=True)

    def action_confirm_rfq(self):
        product = self.product_id
        print("pdt_id",product.id)

        if not product.seller_ids:
            raise UserError("No vendor Found")

        top_vendor = product.seller_ids[0]

        existing_po = self.env['purchase.order'].search([('partner_id', '=', top_vendor.id), ('state', '=', 'draft')], limit=1)

        if existing_po:
            po = existing_po
        else:
            po = self.env['purchase.order'].create([{
                'partner_id': top_vendor.id,
                'date_order': fields.Datetime.now(),
            }])

        existing_line = po.order_line.filtered(lambda o: o.product_id == product and o.price_unit == self.price)
        if existing_line:
            existing_line.product_qty += self.quantity
        else:
            self.env['purchase.order.line'].create([{
                'order_id': po.id,
                'product_id': product.id,
                'product_qty': self.quantity,
                'price_unit': self.price,
                'product_uom_qty': self.quantity,
                'name': product.name,
                'date_planned': fields.Datetime.now(),
            }])
            return {'type': 'ir.actions.act_window_close'}






















            # self.env['purchase.order.line'].filtered(lambda o: o.product_id == product.id))







        # print(existing_po)
        #
        # print("top_vendor", top_vendor)
        # print("po", po)
        #
        # purchase_order = self.env['purchase.order']
        # purchase_order_line = self.env['purchase.order.line']
        #
        #
        # print("action_print")
