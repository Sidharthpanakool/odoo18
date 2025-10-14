# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
from email.policy import default
from odoo import api, fields, models


class ResPartner(models.Model):
    _inherit = "res.partner"

    restricted=fields.Boolean(string="Restricted",store=True)
    restricted_count=fields.Integer(string="Restricted Count",store=True)
