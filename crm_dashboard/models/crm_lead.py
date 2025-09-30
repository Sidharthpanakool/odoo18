from odoo import models, api

class CrmLead(models.Model):
   _inherit = 'crm.lead'


   @api.model
   def get_tiles_data(self):
       company_id = self.env.company
       leads = self.search([('company_id', '=', company_id.id),
                            ('user_id', '=', self.env.user.id)])
       amount_inv=self.env['account.move'].search([])
       # amount_untaxed_in_currency_signed

       print('amount',(amount_inv))
       print('leads',leads)

       my_leads = leads.filtered(lambda r: r.type == 'lead')
       print('myleads',my_leads)

       my_opportunity = leads.filtered(lambda r: r.type == 'opportunity')
       currency = company_id.currency_id.symbol
       expected_revenue = sum(my_opportunity.mapped('expected_revenue'))

       return {
           'total_leads': len(my_leads),
           'total_opportunity': len(my_opportunity),
           'expected_revenue': expected_revenue,
           'currency': currency,
       }
