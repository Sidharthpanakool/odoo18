# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import  fields, models


class ResPartner(models.Model):
    _inherit = "res.partner"

    is_vip = fields.Boolean(string="Is VIP")
    vip_discount = fields.Float(string="VIP Discount %")

