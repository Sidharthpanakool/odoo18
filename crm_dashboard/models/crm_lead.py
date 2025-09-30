from odoo import models, api

class CrmLead(models.Model):
   _inherit = 'crm.lead'

   @api.model
   def get_tiles_data(self):
       company_id = self.env.company
       leads = self.search([('company_id', '=', company_id.id),
                            ('user_id', '=', self.env.user.id)])

       invoices = self.env['account.move'].search([('move_type', '=', 'out_invoice'),('state', '=', 'posted')])

       total_amount_sum = sum(invoice.amount_total for invoice in invoices)

       print("total",total_amount_sum)
       print('invoices',invoices)

       my_leads = leads.filtered(lambda r: r.type == 'lead')
       print('my_leads',my_leads)

       my_opportunity = leads.filtered(lambda r: r.type == 'opportunity')

       print('my_oppertunity',my_opportunity)

       currency = company_id.currency_id.symbol
       expected_revenue = sum(my_opportunity.mapped('expected_revenue'))
       print('currency',currency)
       print('exp_revenue',expected_revenue)

       return {
           'total_leads': len(my_leads),
           'total_opportunity': len(my_opportunity),
           'expected_revenue': expected_revenue,
           'currency': currency,
           'invoice_amt_sum' : total_amount_sum,
       }
