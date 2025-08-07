# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
from odoo import api, fields, models


class WizardVehicleRepairReport(models.TransientModel):
    _name = "wizard.vehicle.repair.report"
    _description = "Wizard Vehicle Repair Report"

    customer_id = fields.Many2many('vehicle.repair', string="Customer")
    start_date = fields.Date(default=fields.date.today())
    delivery_date = fields.Date(string="Delivery Date")
    service_advisor_id = fields.Many2many('res.users',
                                          string="Service Advisor")


    def action_print(self):
        print("action_print")
        report = self.env['vehicle.repair'].search_read([])
        data = {
            'report':report
        }
        print(data,"data")
        return self.env.ref('vehicle_repair_management.action_report_vehicle_repair').report_action(None, data=data)


