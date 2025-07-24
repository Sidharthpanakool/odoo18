# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import fields, models

class VehicleTags(models.Model):
    _name = "vehicle.tags"
    _description = ""

    name = fields.Char(string="Repair Tags")
    color = fields.Integer(string="Color")
