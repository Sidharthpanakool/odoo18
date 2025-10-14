# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
from email.policy import default

from odoo import fields, models


class ProjectTaskType(models.Model):
    _inherit = "project.task.type"

    default_duration=fields.Integer("Default Duration",default=4)
