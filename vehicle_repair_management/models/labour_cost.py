# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models

class LabourCost(models.Model):
    _name = "labour.cost"
    _description = "Labour Cost "

    user_id = fields.Many2one(
        comodel_name='hr.employee',
        string="Employee")

    hourly_cost = fields.Float(string="Hourly Cost")
    worked_hours = fields.Float(string="Worked Hours")
    currency_id = fields.Many2one(related='user_id.currency_id')
    sub_total_cost = fields.Float(string="Sub Total", compute="_compute_total_cost",store=True)

    labour_cost_id = fields.Many2one('vehicle.repair', 'Labour cost id')

    @api.depends('hourly_cost', 'worked_hours')
    def _compute_total_cost(self):
        """For calculating labour cost by multiplying the hourly cost and    worked hours"""
        for record in self:
            record.sub_total_cost = record.hourly_cost * record.worked_hours

