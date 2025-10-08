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

        leads = self.search(domain)
        my_leads = leads.filtered(lambda r: r.type == 'lead')
        my_opportunity = leads.filtered(lambda r: r.type == 'opportunity')
        currency = company_id.currency_id.symbol
        expected_revenue = sum(my_opportunity.mapped('expected_revenue'))

        invoices = self.env['account.move'].search([('move_type', '=', 'out_invoice'),
                                                    ('state', '=', 'posted'),
                                                    ('create_date', '>=', start_date),
                                                    ('create_date', '<=', end_date)])
        total_amount_sum = sum(invoice.amount_total for invoice in invoices)

        won = self.search(
            [('company_id', '=', company_id.id), ('user_id', '=', self.env.user.id), ('stage_id.is_won', '=', True),
             ('active', '=', True), ('probability', '=', 100),
             ('create_date', '>=', start_date),
             ('create_date', '<=', end_date)
             ])
        loss = self.search(
            [('company_id', '=', company_id.id), ('user_id', '=', self.env.user.id), ('stage_id.is_won', '=', False),
             ('active', '=', False), ('probability', '=', 0),
             ('create_date', '>=', start_date),
             ('create_date', '<=', end_date)
             ])


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
            'my_leads': my_leads.ids,
            'my_opportunity': my_opportunity.ids,
            'leads': leads,
            'lost_vs_won': {'Won': won, 'Lost': loss},
            'start_date': start_date,
            'end_date': end_date,

        }

    @api.model
    def get_chart_data(self):
        filter_type = self.env.context.get('filter', 'year')
        start_date, end_date = self._get_date_range(filter_type)

        user = self.env.user.id
        company_id = self.env.company

        lost_count = self.search_count([
            ('user_id', '=', user),
            ('stage_id.is_won', '=', False),
            ('active', '=', False),
            ('create_date', '>=', start_date),
            ('create_date', '<=', end_date)
        ])



        won_count = self.search_count([
            ('user_id', '=', user),
            ('stage_id.is_won', '=', True),
            ('create_date', '>=', start_date),
            ('create_date', '<=', end_date)
        ])

        activity_data = self.env['mail.activity'].read_group(
            [('user_id', '=', user),
             ('create_date', '>=', start_date),
             ('create_date', '<=', end_date)],
            ['activity_type_id'], ['activity_type_id']
        )

        activities = {
            act['activity_type_id'][1]: act['activity_type_id_count']
            for act in activity_data if act['activity_type_id']
        }


        leads_by_month = self.read_group([('type', '=', 'lead'),
                                          ('create_date', '>=', start_date),
                                          ('create_date', '<=', end_date),
                                          ('user_id', '=', user)],
                                         ['id:count', 'create_date: month'],
                                         ['create_date'],
                                         orderby='create_date:month')

        leads_by_medium = self.read_group(
            [('type', '=', 'lead'), ('user_id', '=', user),
             ('create_date', '>=', start_date),
             ('create_date', '<=', end_date)],
            ['medium_id'], ['medium_id']
        )

        leads_by_campaign = self.read_group(
            [('type', '=', 'lead'), ('user_id', '=', user),
             ('create_date', '>=', start_date),
             ('create_date', '<=', end_date)],
            ['campaign_id'], ['campaign_id']
        )

        return {

            'lost_vs_won': {'Won': won_count, 'Lost': lost_count},
            'activity': activities,
            'leads_by_medium': { r['medium_id'][1] if r['medium_id'] else 'Unknown': r['medium_id_count']
                                for r in leads_by_medium
            },
            'leads_by_campaign': { r['campaign_id'][1] if r['campaign_id'] else 'No Campaign': r['campaign_id_count']
                                for r in leads_by_campaign
            },
            'leads_by_month': [
                {'month': r['create_date'], 'count': r['create_date_count']}
                for r in leads_by_month
            ],
        }

    def _get_date_range(self, filter_type):
        today = date.today()
        if filter_type == 'year':
            start = date(today.year, 1, 1)

        elif filter_type == 'quarter':
            q = (today.month - 1) // 3 + 1
            start = date(today.year, 3 * (q - 1) + 1, 1)

        elif filter_type == 'month':
            start = date(today.year, today.month, 1)

        elif filter_type == 'week':
            start = today - timedelta(days=today.weekday())

        else:
            start = date(today.year, 1, 1)

        return start, today
