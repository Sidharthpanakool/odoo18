# Part of Odoo. See LICENSE file for full copyright and licensing details.
from odoo import api,fields, models

class SurveySurvey(models.Model):
    _inherit = 'survey.survey'
    _description = 'Survey'

    quiz_idle_time=fields.Boolean()
    idle_time_limit = fields.Integer("Time limit (minutes)", default=10)
