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




       # activity_data = self.env['mail.activity'].read_group(
       #     [('user_id', '=', user)],
       #     ['activity_type_id'], ['activity_type_id']
       # )
       # print("activity_data",activity_data)
       # activities = {
       #     act['activity_type_id'][1]: act['activity_type_id_count']
       #     for act in activity_data if act['activity_type_id']
       # }
       # print("activities",activities)
       # # leads_by_month = self.env['crm.lead'].read_group(
       # #     [('user_id', '=', user), ('create_date', '>=', start_date), ('create_date', '<=', end_date)],
       # #     ['id:count', 'create_date:month'], ['create_date:month'], orderby='create_date:month'
       # # )
       # # print("leads_by_month",leads_by_month)
       # leads_by_medium = self.env['crm.lead'].read_group(
       #     [('user_id', '=', user)],
       #     ['medium_id'], ['medium_id']
       # )
       # print("leads_by_medium",leads_by_medium)
       #
       # leads_by_campaign = self.env['crm.lead'].read_group(
       #     [('user_id', '=', user)],
       #     ['campaign_id'], ['campaign_id']
       # )
       # print("leads_by_campaign",leads_by_campaign)




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
           'leads':leads,
           'lost_vs_won': {'Won': won, 'Lost': loss},
       }


   def get_chart_data(self, filter_type='year'):
       start, end = self._get_date_range(filter_type)
       crm_lead = self.env['crm.lead']
       user = self.env.user

       lost_count = crm_lead.search_count([
           ('user_id', '=', user.id),
           ('stage_id.is_won', '=', False),
           ('active', '=', False)
       ])
       won_count = crm_lead.search_count([
           ('user_id', '=', user.id),
           ('stage_id.is_won', '=', True)
       ])

       activity_data = self.env['mail.activity'].read_group(
           [('user_id', '=', user.id)],
           ['activity_type_id'], ['activity_type_id']
       )
       print("activity_data")
       activities = {
           act['activity_type_id'][1]: act['activity_type_id_count']
           for act in activity_data if act['activity_type_id']
       }
       print("activities")
       # leads_by_month = self.env['crm.lead'].read_group(
       #     [('user_id', '=', user.id), ('create_date', '>=', start), ('create_date', '<=', end)],
       #     ['id:count', 'create_date:month'], ['create_date:month'], orderby='create_date:month'
       # )
       # print("leads_by_month")
       leads_by_medium = self.env['crm.lead'].read_group(
           [('user_id', '=', user.id)],
           ['medium_id'], ['medium_id']
       )
       print("leads_by_medium")

       leads_by_campaign = self.env['crm.lead'].read_group(
           [('user_id', '=', user.id)],
           ['campaign_id'], ['campaign_id']
       )
       print("leads_by_campaign")

       return {
           'lost_vs_won': {'Won': won_count, 'Lost': lost_count},
           'activity': activities,

           'leads_by_medium': {
               r['medium_id'][1] if r['medium_id'] else 'Unknown': r['medium_id_count']
               for r in leads_by_medium
           },
           'leads_by_campaign': {
               r['campaign_id'][1] if r['campaign_id'] else 'No Campaign': r['campaign_id_count']
               for r in leads_by_campaign
           },
       }

   # 'leads_by_month': [
   #     {'month': r['create_date:month'], 'count': r['create_date:month_count']}
   #     for r in leads_by_month
   # ],

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