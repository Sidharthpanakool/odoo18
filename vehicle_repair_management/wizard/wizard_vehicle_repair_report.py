# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
from email.policy import default

from odoo import api, fields, models

class WizardVehicleRepairReport(models.TransientModel):
    _name = "wizard.vehicle.repair.report"
    _description = "Wizard Vehicle Repair Report"

    customer_id=fields.Many2one('vehicle.repair',
                                string="Customer")
    start_date = fields.Date(default=fields.date.today())
    delivery_date = fields.Date(string="Delivery Date")
    vehicle_type = fields.Many2one('fleet.vehicle.model.category',
                                   string="Vehicle Type")
    vehicle_model = fields.Many2one('fleet.vehicle.model',
                                    string="Vehicle Model",
                                    domain="[('category_id','=',vehicle_type)]"
                                    )
    # domain = "[('vehicle_type','=',vehicle_type)]"
    vehicle_number = fields.Char(string="Vehicle Number",
                                 domain = '[("customer_id", "=", name)]',
                                 )
    service_advisor_id = fields.Many2one('res.users',
                                         string="Service Advisor")

