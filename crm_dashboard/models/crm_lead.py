from datetime import date, timedelta
from dateutil.relativedelta import relativedelta
from odoo import models, api

class CrmLead(models.Model):
   _inherit = 'crm.lead'

   @api.model
   def get_tiles_data(self):
       company_id = self.env.company
       user=self.env.user.id

       filter_type = self.env.context.get('filter', 'year')
       start_date, end_date = self._get_date_range(filter_type)

       domain = [('company_id', '=', company_id.id),
                 ('user_id', '=', user),
                 ('create_date', '>=', start_date),
                 ('create_date', '<=', end_date)]

       is_manager = self.env.user.has_group('sales_team.group_sale_manager')

       if not is_manager:
           domain.append(('user_id', '=', user))

       print('company_id',company_id)
       print('users',user)

       leads=self.search(domain)
       # leads = self.search([('company_id', '=', company_id.id),('user_id', '=', user)])
       my_leads = leads.filtered(lambda r: r.type == 'lead')

       print("leads",leads)
       print('my_leads', my_leads)

       invoices = self.env['account.move'].search([('move_type', '=', 'out_invoice'),('state', '=', 'posted')])
       total_amount_sum = sum(invoice.amount_total for invoice in invoices)

       print('invoices', invoices)
       print("total",total_amount_sum)

       my_opportunity = leads.filtered(lambda r: r.type == 'opportunity')

       print('my_oppertunity',my_opportunity)

       currency = company_id.currency_id.symbol
       expected_revenue = sum(my_opportunity.mapped('expected_revenue'))

       print('currency',currency)
       print('exp_revenue',expected_revenue)

       won =self.search([('company_id', '=', company_id.id),('user_id', '=', self.env.user.id),('stage_id', '=', 4),('active','=',True),('probability','=',100)])
       # .with_context(active_test=False)
       loss=self.search([('company_id', '=', company_id.id),('user_id', '=', self.env.user.id),('stage_id', '!=',4),('active','=',False),('probability','=',  0)])

       print(won)
       print('won',len(won))
       print(loss)
       print('loss',len(loss))

       return {
           'total_leads': len(my_leads),
           'total_opportunity': len(my_opportunity),
           'expected_revenue': expected_revenue,
           'currency': currency,
           'invoice_amt_sum': total_amount_sum,
           'won': len(won),
           'loss': len(loss),
           'company_id': company_id,
           'user': user,
           'my_leads': my_leads,
           'my_opportunity': my_opportunity,
           'leads':leads
       }


   def _get_date_range(self, filter_type):
       today = date.today()
       if filter_type == 'year':
           start = date(today.year, 1, 1)
           print(start)

       elif filter_type == 'quarter':
           q = (today.month - 1) // 3 + 1
           start = date(today.year, 3 * (q - 1) + 1, 1)
           print(start)

       elif filter_type == 'month':
           start = date(today.year, today.month, 1)
           print(start)

       elif filter_type == 'week':
           start = today - timedelta(days=today.weekday())
           print(start)

       else:
           start = date(today.year, 1, 1)
           print(start)

       return start, today