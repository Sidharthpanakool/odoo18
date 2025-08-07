# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
from odoo import api, fields, models


class WizardVehicleRepairReport(models.TransientModel):
    _name = "wizard.vehicle.repair.report"
    _description = "Wizard Vehicle Repair Report"

    customer_id = fields.Many2many('vehicle.repair', string="Customer")
    start_date = fields.Date(default=fields.date.today())
    delivery_date = fields.Date(string="Delivery Date")
    vehicle_type = fields.Many2one('fleet.vehicle.model.category', string="Vehicle Type")
    vehicle_model = fields.Many2one('fleet.vehicle.model', string="Vehicle Model",
                                    domain="[('category_id','=',vehicle_type)]")
    # domain = "[('vehicle_type','=',vehicle_type)]"
    vehicle_number = fields.Char(string="Vehicle Number",
                                 domain='[("name", "=", customer_id)]')
    service_advisor_id = fields.Many2many('res.users',
                                          string="Service Advisor")
    total_cost = fields.Char(String="Total Cost")

    service_type = fields.Selection(
        string="Service Type",
        selection=[('free', 'Free'), ('paid', 'Paid')]
    )
    estimated_amt = fields.Float(string="Estimated Amount")

    def action_print(self):
        print("action_print")
        data = {
            'start_date':self.start_date
        }
        print(data)
        return self.env.ref('vehicle_repair_management.action_report_vehicle_repair').report_action(None, data=data)



# data = {
#     'model_id': self.id,
#     'customer_id': self.customer_id,
#     'start_date': self.start_date
# }
# docids = self.env['purchase.order'].search([]).ids
# return self.env.ref('WizardVehicleRepairReport.action_report_vehicle_repair').report_action(None, data=data)


# def action_print(self):
#     vehicle_report=self.env['vehicle.repair'].search_read([])
#     data={
#         'form':self.read()[0],
#         'report':vehicle_report,
#     }
#     return self.env.ref('custom_report.vehicle_repair_report').report_action(self,data=data)
