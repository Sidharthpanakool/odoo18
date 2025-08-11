# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
from odoo import api, fields, models


class WizardVehicleRepairReport(models.TransientModel):
    _name = "wizard.vehicle.repair.report"
    _description = "Wizard Vehicle Repair Report"

    vehicle_repair_id = fields.Many2many('res.partner', string="Customer")
    start_date = fields.Date(default=fields.date.today())
    end_date = fields.Date(string="End Date")
    service_advisor = fields.Many2many('res.users',
                                          string="Service Advisor")


    def action_print(self):
        print("action_print")
        report = self.env['vehicle.repair'].search_read([])
        data = {
            'customer_id':self.vehicle_repair_id.ids,
            'start_date':self.start_date,
            'delivery_date':self.end_date,
            'service_advisor_id':self.service_advisor.ids,

        }
        print("customer_id",data["customer_id"])
        print("service_advisor_id",data["service_advisor_id"])
        print(data)

        return self.env.ref('vehicle_repair_management.action_report_vehicle_repair').report_action(None, data=data)


