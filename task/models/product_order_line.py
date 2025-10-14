# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import api, models,fields


class PurchaseOrderLine(models.Model):
    _inherit = 'purchase.order.line'

