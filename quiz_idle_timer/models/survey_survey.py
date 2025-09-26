# Part of Odoo. See LICENSE file for full copyright and licensing details.
from odoo import api,fields, models

class SurveySurvey(models.Model):
    _inherit = 'survey.survey'
    _description = 'Survey'

    quiz_idle_time=fields.Boolean()
    idle_time_limit = fields.Float("Time limit (minutes)", default=.16)


    # @api.model
    # def get_data_for_js(self):
    #     # Example: Fetch all records and return their name and value
    #     records = self.search([])
    #     data = []
    #     for rec in records:
    #         data.append({
    #             'id': rec.id,
    #             'quiz_idle_time': rec.time,
    #             'idle_time_limit': rec.time_limit,
    #         })
    #         print(data)
    #     return data
