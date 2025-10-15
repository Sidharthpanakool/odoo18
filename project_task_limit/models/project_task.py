# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
from odoo import api, models
from odoo.exceptions import ValidationError

class ProjectTask(models.Model):
    _inherit = "project.task"

    @api.model_create_multi
    def create(self, vals_list):
        tasks = super().create(vals_list)
        tasks._check_user_task_limit()
        return tasks

    def write(self, vals):
        res = super().write(vals)
        if 'user_ids' in vals:
            self._check_user_task_limit()
        return res

    def _check_user_task_limit(self):
        limit = float(self.env['ir.config_parameter'].sudo().get_param('project_task_limit.open_task_limit', 10))
        users=self.user_ids
        if not users:
            return
        for user in users:
            open_count = self.env['project.task'].search_count([('user_ids', 'in', user.id),('stage_id.fold', '=', False)])
            if open_count > limit:
                raise ValidationError(f"User {user.name} already has {open_count} open tasks (limit: {int(limit)}).")