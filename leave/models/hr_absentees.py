# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
import datetime

from dateutil.utils import today
from odoo import api, models, fields
from odoo.tools import date_utils


class HrAbsentees(models.Model):
    _name = "hr.absentees"
    _description = "Attendance"

    name = fields.Date(default=lambda *a: fields.Date.today(),
                       string="Date",
                       required=True)

    employee_ids = fields.Many2one('hr.employee',
                                   string="Employee")



    @api.model
    def generate_daily_absentees(self):
        # Get all employees
        all_employees = self.env['hr.employee'].search([])
        # Get employees who have already checked in today
        attendance_model = self.env['hr.attendance']
        attended_today = attendance_model.search([
            ('check_in', '>', today()),

        ])
        attended_emp_ids = set(attended_today.mapped('employee_id.id'))
        absent_emps = all_employees.filtered(lambda emp: emp.id not in attended_emp_ids)


        for rec in all_employees:
            if rec.id not in attended_emp_ids and not self.env['hr.absentees'].search([('employee_ids','=',rec.id)]):
                self.create({
                    'employee_ids': rec.id,
                })


    def unlink(self):
        attendance_model = self.env['hr.attendance']
        now = fields.Datetime.now()

        for record in self:
            for emp in record.employee_ids:
                attendance_model.create({
                    'employee_id': emp.id,
                    'check_in': now,
                })
        return super(HrAbsentees, self).unlink()

