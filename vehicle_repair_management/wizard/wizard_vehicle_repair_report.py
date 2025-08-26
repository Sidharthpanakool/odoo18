# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
import io
import json
import xlsxwriter
from odoo import models
from odoo.tools import json_default, date_utils
from odoo import api, fields, models
from odoo.addons.test_convert.tests.test_env import record


class WizardVehicleRepairReport(models.TransientModel):
    _name = "wizard.vehicle.repair.report"
    _description = "Wizard Vehicle Repair Report"

    vehicle_repair_id = fields.Many2many('res.partner', string="Customer")
    start_date = fields.Date(default=fields.date.today())
    end_date = fields.Date(string="End Date")
    service_advisor = fields.Many2many('res.users',
                                       string="Service Advisor")

    def action_print(self):
        report = self.env['vehicle.repair'].search_read([])
        data = {
            'customer_id': self.vehicle_repair_id.ids,
            'start_date': self.start_date,
            'delivery_date': self.end_date,
            'service_advisor_id': self.service_advisor.ids,
        }
        return self.env.ref('vehicle_repair_management.action_report_vehicle_repair').report_action(None, data=data)


    def vehicle_repair_report_excel(self):
        record = self.env['vehicle.repair'].search_read([])
        data = {
            'customer_id': self.vehicle_repair_id.ids,
            'start_date': self.start_date,
            'delivery_date': self.end_date,
            'service_advisor_id': self.service_advisor.ids,

        }
        return {
            'type': 'ir.actions.report',
            'data': {'model': 'report.vehicle_repair_management.vehicle_repair_report',
                     'options': json.dumps(data,
                                           default=json_default),
                     'output_format': 'xlsx',
                     'report_name': 'Vehicle Repair Excel Report',
                     },
            'report_type': 'xlsx',
        }
