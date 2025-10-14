# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
import typing
from dataclasses import fields
from datetime import timedelta

from odoo import api, models, fields
from odoo.exceptions import ValidationError


class ProjectTask(models.Model):
    _inherit = "project.task"

    @api.model
    def create(self,vals):
        N=10

        my_open_tasks=self.search_count([('stage_id', 'not in', ['1_done', '1_cancelled']),('write_uid','=',self.env.uid)])
        if my_open_tasks>N:
            raise ValidationError('Your open project limit exceeded')
        return super().write(vals)

    def write(self, vals):
        N = 10
        assignee=self.user_ids
        print("assignee",assignee)
        task=[]
        if assignee:
            for rec in assignee:
                my_open_tasks = self.search([('stage_id', 'not in', ['1_done', '1_cancelled']),('user_ids','=',rec.id)])
                task.append(my_open_tasks)

                print(task)
                # if task>N:
                #     print("Hiiii")




        # @api.model
        # def create(self, vals):
        #     N = 10
        #     assigned_user = vals.get('user_id') or self.env.user.id
        #     open_tasks = self.search_count([
        #         ('stage_id', 'not in', ['1_done', '1_cancelled']),
        #         ('user_id', '=', assigned_user)
        #     ])
        #     if open_tasks >= N:
        #         raise ValidationError('This user has reached the open task limit.')
        #     return super().create(vals)

        # def write(self, vals):
        #     N = 10
        #     # Only check when assigning/reassigning a user
        #     if 'user_id' in vals and vals['user_id']:
        #         assigned_user = vals['user_id']
        #         open_tasks = self.search_count([
        #             ('stage_id', 'not in', ['1_done', '1_cancelled']),
        #             ('user_id', '=', assigned_user)
        #         ])
        #         if open_tasks >= N:
        #             raise ValidationError('This user has reached the open task limit.')
        #     return super().write(vals)









































    # @api.onchange('stage_id')
    # def _deadline_change(self):
    #     today = fields.Datetime.today()
    #     days = self.env['project.task.type'].search([('id', '=', self.stage_id.id)])
    #     days = days.default_duration
    #
    #     print("today", today)
    #     print('days', days)
    #     self.date_deadline = today + timedelta(days=days)
    #     print('s', self.date_deadline)




        # if self.date_deadline==False or self.date_deadline==True:

        # if days:
        # for rec in days:
        #     self.date_deadline=today+timedelta(days=rec.default_duration)
        #     print('self.date_deadline',self.date_deadline)


    # def write(self,vals):
    #     for order in self:
    #         today = fields.Datetime.today()
    #         days = self.env['project.task.type'].search([('id', '=', order.stage_id.id)])
    #         days = days.default_duration
    #
    #         print('days', days)
    #         print('s', order.date_deadline)
    #
    #         # print(today + timedelta(days=days), vals)
    #
    #         vals['date_deadline'] = today + timedelta(days=days)
    #         print("V",vals)
    #
    #     return super().write(vals)