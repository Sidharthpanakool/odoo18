# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import models


class ProductProduct(models.Model):
    _inherit = "product.product"

    def action_create_po(self):

        product = self.product_variant_id
        return {
            'name': 'Create RFQ',
            'type': 'ir.actions.act_window',
            'res_model': 'wizard.product.product',
            'view_mode': 'form',
            'target': 'new',
            'context': {
                'default_product_id': product.id,
            }
        }
