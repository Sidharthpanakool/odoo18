# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
from odoo import fields, models


class ResPartner(models.Model):
    _inherit = "res.partner"

    restricted = fields.Boolean(string="Restricted")
    restricted_count = fields.Integer(string="Restricted Count",store=True)
