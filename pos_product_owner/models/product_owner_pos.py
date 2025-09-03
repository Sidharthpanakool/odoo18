# -*- coding: utf-8 -*-
from odoo import fields,models,api

class ProductOwnerPos(models.Model):
    _inherit = "product.template"

    product_owner_id=fields.Many2one('res.partner',string="Product Owner",required=True)

