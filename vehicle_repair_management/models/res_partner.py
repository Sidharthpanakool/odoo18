# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
from email.policy import default
from odoo import api, fields, models


class ResPartner(models.Model):
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

    customer_status = fields.Selection([
        ('non_service', 'Non Service Customer'),
        ('service', 'Service Customer')
    ], default='non_service',
        string='Customer Status',

    )
    # compute="_compute_customer_status"

    # @api.model
    # def _compute_customer_status(self):
    #     for rec in self:
    #         if rec.vehicle_service >= 1:
    #             rec.customer_status = 'service'
    #         else:
    #             rec.customer_status = 'non_service'

    def button_service_customer(self):
        print('button_service_customer')

        return {
            'name': 'service customer',
            'type': 'ir.actions.act_window',
            'view_type': 'form',
            'view_mode': 'form',
            'res_model': 'res.partner',
            'view_id': self.env.ref('vehicle_repair_management.action_service_customer_form_view').id,
            'target': 'current',
            'context': {'create': False,
                        'default_name': self.name,
                        'default_phone': self.phone,
                        'default_image_1920': self.image_1920
                        }
        }

