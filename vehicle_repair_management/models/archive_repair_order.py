# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
from email.policy import default

from odoo import api, fields, models
from datetime import datetime, timedelta
from odoo.exceptions import AccessError, UserError, ValidationError

from dateutil.relativedelta import relativedelta


class ArchiveRepairOrder(models.Model):
    _name = "archive.repair.order"
    _description = "Archive Repair Order"

    @api.model
    def auto_archive_order(self):
        orders=self.env['vehicle.repair'].search([('date_order','<',fields.Datetime.subtract(fields.Datetime.now(),months=1)),
                                                  ('state', 'in',['cancelled'])])
        for order in orders:
            order.write({'active':False})