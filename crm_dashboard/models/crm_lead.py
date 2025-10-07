import calendar
from datetime import date, timedelta
from dateutil.relativedelta import relativedelta
from odoo import models, api


class CrmLead(models.Model):
    _inherit = 'crm.lead'

    @api.model
    def get_tiles_data(self):
        company_id = self.env.company
        user = self.env.user.id

        filter_type = self.env.context.get('filter', 'year')
        start_date, end_date = self._get_date_range(filter_type)

        domain = [('company_id', '=', company_id.id),
                  ('user_id', '=', user),
                  ('create_date', '>=', start_date),
                  ('create_date', '<=', end_date)]

        is_manager = self.env.user.has_group('sales_team.group_sale_manager')

        if not is_manager:
            domain.append(('user_id', '=', user))

        # print('company_id',company_id)
        # print('users',user)

        leads = self.search(domain)
        # leads = self.search([('company_id', '=', company_id.id),('user_id', '=', user)])
        my_leads = leads.filtered(lambda r: r.type == 'lead')

        # print("leads",leads)
        # print('my_leads', my_leads)

        invoices = self.env['account.move'].search([('move_type', '=', 'out_invoice'), ('state', '=', 'posted'),('create_date', '>=', start_date),
                  ('create_date', '<=', end_date)])
        total_amount_sum = sum(invoice.amount_total for invoice in invoices)

        # print('invoices', invoices)
        # print("total",total_amount_sum)

        my_opportunity = leads.filtered(lambda r: r.type == 'opportunity')

        # print('my_oppertunity',my_opportunity)

        currency = company_id.currency_id.symbol
        expected_revenue = sum(my_opportunity.mapped('expected_revenue'))

        # print('currency',currency)
        # print('exp_revenue',expected_revenue)

        won = self.search([('company_id', '=', company_id.id), ('user_id', '=', self.env.user.id), ('stage_id', '=', 4),
                           ('active', '=', True), ('probability', '=', 100),
                           ('create_date', '>=', start_date),
                           ('create_date', '<=', end_date)
                           ])
        # .with_context(active_test=False)
        loss = self.search(
            [('company_id', '=', company_id.id), ('user_id', '=', self.env.user.id), ('stage_id', '!=', 4),
             ('active', '=', False), ('probability', '=', 0),
             ('create_date', '>=', start_date),
             ('create_date', '<=', end_date)
             ])

        # print(won)
        # print('won',len(won))
        # print(loss)
        # print('loss',len(loss))

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
            'leads': leads,
            'lost_vs_won': {'Won': won, 'Lost': loss},
        }

    def get_chart_data(self):
        filter_type = self.env.context.get('filter', 'year')
        start_date, end_date = self._get_date_range(filter_type)

        user = self.env.user.id
        company_id = self.env.company

        domain = [('company_id', '=', company_id.id),
                  ('user_id', '=', user),
                  ('create_date', '>=', start_date),
                  ('create_date', '<=', end_date)]

        # leads = self.search(domain)
        # # leads = self.search([('company_id', '=', company_id.id),('user_id', '=', user)])
        # my_leads = leads.filtered(lambda r: r.type == 'lead')

        lost_count = self.search_count([
            ('user_id', '=', user),
            ('stage_id.is_won', '=', False),
            ('active', '=', False),
            ('create_date', '>=', start_date),
            ('create_date', '<=', end_date)
        ])

        # print("lost_count",lost_count)

        won_count = self.search_count([
            ('user_id', '=', user),
            ('stage_id.is_won', '=', True),
            ('create_date', '>=', start_date),
            ('create_date', '<=', end_date)
        ])
        # print("won_count",won_count)

        activity_data = self.env['mail.activity'].read_group(
            [('user_id', '=', user),
             ('create_date', '>=', start_date),
             ('create_date', '<=', end_date)],
            ['activity_type_id'], ['activity_type_id']
        )
        # print("activity_data",activity_data)

        activities = {
            act['activity_type_id'][1]: act['activity_type_id_count']
            for act in activity_data if act['activity_type_id']
        }

        # print("activities",activities)

        leads_month = self.search([('type', '=', 'lead'),('create_date', '<=', end_date),('create_date', '>=', start_date), ('user_id', '=', user)])
        lead_month_ ={}
        print("lll", len(leads_month))

        # count=1
        # for records in leads_month:
        #     date=records.create_date
        #     month_name=calendar.month_name[date.month]
        #     # print("mo",month_name)
        #     if month_name not in leads_month:
        #         lead_month_[month_name]=count
        #
        #     else:
        #         lead_month_[month_name] = lead_month_[month_name]+1
        #     print("mo", month_name)
        #     print("lala",lead_month_[month_name])




        leads_by_month=self.read_group([('type', '=', 'lead'),('create_date', '>=', start_date),('create_date', '<=', end_date), ('user_id', '=', user)],
                                       ['id:count', 'create_date: month'],
                                       ['create_date'],
                                       orderby='create_date:month'
                                       )
        # print("a",a)



        # leads_by_month = self.read_group(
        #     [('user_id', '=', user), ('create_date', '>=', start_date), ('create_date', '<=', end_date)],
        #     ['id:count', 'create_date: month'], ['create_date:month'], orderby='create_date:month'
        # )
        print("leads_by_month", len(leads_by_month))

        leads_by_medium = self.read_group(
            [('type', '=', 'lead'),('user_id', '=', user), ('create_date', '>=', start_date),
             ('create_date', '<=', end_date)],
            ['medium_id'], ['medium_id']
        )
        print("leads_by_medium", leads_by_medium)

        leads_by_campaign = self.read_group(
            [('type', '=', 'lead'),('user_id', '=', user),
             ('create_date', '<=', end_date)],
            ['campaign_id'], ['campaign_id']
        )
        print("leads_by_campaign", leads_by_campaign)

        # report = self.env.cr.dictfetchall()
        # print('report',report)

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
            'leads_by_month': [
                {'month': r['create_date'], 'count': r['create_date_count']}
                for r in leads_by_month
            ],
        }

    # 'leads_by_month': [
    #     {'month': r['create_date:month'], 'count': r['create_date:month_count']}
    #     for r in leads_by_month
    # ],
    # 'docs': report,
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
