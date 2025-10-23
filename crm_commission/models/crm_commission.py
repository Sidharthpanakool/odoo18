import calendar
from datetime import date, timedelta
from dateutil.relativedelta import relativedelta
from odoo import models, fields, api

class CrmCommission(models.Model):
    _name = "crm.commission"

    name = fields.Char(string="Name")
    active = fields.Boolean(string="Active")
    from_date = fields.Datetime(string="From Date")
    to_date = fields.Datetime(string="To Date")
    type = fields.Selection([
        ('by_product','Product Wise'),
        ('by_revenue','Revenue Wise')
    ],string="Type")

