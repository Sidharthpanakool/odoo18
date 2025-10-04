from odoo import models

from odoo import api,fields,models

class SaleOrder(models.Model):
    _inherit = "sale.order"

    def action_confirm(self):
        res = super().action_confirm()

        for order in self:
            if order.opportunity_id and order.team_id and order.team_id.lead_state_id:
                if order.opportunity_id.stage_id != order.team_id.lead_state_id:
                    order.opportunity_id.stage_id = order.team_id.lead_state_id
                return res