# Part of Odoo. See LICENSE file for full copyright and licensing details.
from odoo import api,fields, models

class SurveySurvey(models.Model):
    _inherit = 'survey.survey'
    _description = 'Survey'

    quiz_idle_time=fields.Boolean()
    idle_time_limit = fields.Float("Time limit (minutes)", default=.25)


 # @api.onchange('session_speed_rating', 'session_speed_rating_time_limit')
 #    def _onchange_session_speed_rating(self):
 #        """Show impact on questions in the form view (before survey is saved)."""
 #        for survey in self.filtered('question_ids'):
 #            survey.question_ids._update_time_limit_from_survey(
 #                is_time_limited=survey.session_speed_rating, time_limit=survey.session_speed_rating_time_limit)