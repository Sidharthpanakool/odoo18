from odoo import api,fields,models

class CrmTeam(models.Model):
    _inherit = 'crm.team'

    lead_state_id=fields.Many2one('crm.stage',string='Default Lead Stage')