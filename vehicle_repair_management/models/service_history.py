# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models


class ServiceHistory(models.Model):
    _inherit = "res.partner"

    vehicle_service = fields.Integer(string="Service History", compute='service_history',
                                     default=0)

    def service_history(self):
        """For calculating count and for fetching service history"""
        for record in self:
            record.vehicle_service = self.env['vehicle.repair'].search_count([('name', '=', self.id)])

    def action_get_service_history(self):
        """For fetching service history"""
        self.ensure_one()
        return {
            'type': 'ir.actions.act_window',
            'name': 'Service History',
            'view_mode': 'list',
            'res_model': 'vehicle.repair',
            'domain': [('name', '=', self.id)],
            'context': "{'create': True}"
        }

    def action_archive(self):
        res = super().action_archive()
        repairs = (self.env['vehicle.repair'].with_context(active_test=False).search([('name', 'in', self.ids)]))
        repairs.write({'active': False})
        return res

    def action_unarchive(self):
        res = super().action_unarchive()
        repairs = self.env['vehicle.repair'].with_context(active_test=False).search([('name', 'in', self.ids)])
        repairs.write({'active': True})
        return res



