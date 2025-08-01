# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
import datetime

from odoo import api,models,fields
class Attendance(models.Model):
    _name = "attendance"
    _description = "Attendance"

    name=fields.Many2one('hr.employee',string="Employee")
    check_in=fields.Datetime("Check In")
    check_out=fields.Datetime("Check Out")


    def absenteee(self):
        employee_absentee_list=[]
        absentees=self.erv['hr_attendance']

