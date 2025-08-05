# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
from odoo import api, fields, models

class WizardVehicleRepairReport(models.TransientModel):
    _name = "wizard.vehicle.repair.report"
    _description = "Wizard Vehicle Repair Report"

    customer_id=fields.Many2one('vehicle.repair',string="Customer")
    start_date = fields.Date(default=fields.date.today())
    delivery_date = fields.Date(string="Delivery Date")
    vehicle_type = fields.Many2one('fleet.vehicle.model.category',string="Vehicle Type")
    vehicle_model = fields.Many2one('fleet.vehicle.model',string="Vehicle Model",
                                    domain="[('category_id','=',vehicle_type)]")
    # domain = "[('vehicle_type','=',vehicle_type)]"
    vehicle_number = fields.Char(string="Vehicle Number",
                                 domain = '[("name", "=", customer_id)]')
    service_advisor_id = fields.Many2one('res.users',
                                         string="Service Advisor")

    def action_print(self):
        data={
            # 'model_id':self.id,
            'customer_id':self.customer_id,
            'start_date':self.start_date
        }
        # docids = self.env['purchase.order'].search([]).ids
        return self.env.ref('wizard.vehicle.repair.report.vehicle_repair_report').report_action(None, data=data)

    # @api.model
    # def _get_report_values(self, docids, data=None):
    #     docs = self.env[model.model].browse(docids)
    #     return {
    #         'doc_ids': docids,
    #         'doc_model': model.model,
    #         'docs': docs,
    #         'data': data,
    #     }

    # def action_print(self):
    #     vehicle_report=self.env['vehicle.repair'].search_read([])
    #     data={
    #         'form':self.read()[0],
    #         'report':vehicle_report,
    #     }
    #     return self.env.ref('custom_report.vehicle_repair_report').report_action(self,data=data)