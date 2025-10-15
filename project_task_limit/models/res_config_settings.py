from odoo import fields, models
class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    open_task_limit = fields.Integer('Task Limit',default=10,config_parameter='project_task_limit.open_task_limit')


