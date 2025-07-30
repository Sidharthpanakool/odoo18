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
        string='Customer Status'
    )

    def status_change(self):
        self.customer_status.write('customer_status', 'service')


    def button_service_customer(self):
        print('button_service_customer')

        # self.ensure_one()
        # return {
        #     'type': 'ir.actions.act_window',
        #     'name': 'Service Customer',
        #     'view_mode': 'Form',
        #     'res_model': 'vehicle.repair',
        #     'domain': [('vehicle_service', '=', self.id)],
        #     'context': "{'create': True}"
        # }

        # return {
        #     'type': 'ir.actions.act_window',
        #     'res_model': 'account.move',
        #     'res_id': self.invoice_id.id,
        #     'view_mode': 'form',
        #       'context': {
        #         'name': self.id,
        #         'phone': self.id,
        #
        #     },
        #
        # }

        # for rec in self.customer_status:
        #     if rec.customer_status=="service":


        # compute = "_compute_customer_status"

        # @api.model
        # def write(self,):
        #     self.customer_status.write("customer_status":'service')

        # @api.model
        # def automated_action_select_customer_status(self):
        #     self.customer_status('customer_status':"service")
        #
        # @api.model
        # def _compute_customer_status(self):
        #     for rec in self:
        #         if rec.vehicle_service >= 1:
        #             rec.customer_status = 'service'
        #         else:
        #             rec.customer_status = 'non_service'
