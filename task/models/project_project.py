# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import api, models,fields


class ProjectProject(models.Model):
    _inherit = "project.project"

    progress=fields.Float('Progress(%)',compute='_compute_percentage')


    def _compute_percentage(self):
        total_task = self.env['project.task'].search_count([('project_id', '=', self.id)])
        done_task = self.env['project.task'].search_count([('project_id', '=', self.id), ('stage_id', '=', 3)])
        self.progress = (done_task / total_task)

        print("t", total_task)
        print('d', done_task)
        print((done_task / total_task) * 100)



