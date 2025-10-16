# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models, _
from odoo.api import onchange


class PurchaseOrder(models.Model):
    _inherit = "purchase.order"


    @api.model
    def action_cron_test_po_delayed(self):
        print(fields.datetime.today())
        print("fi",self.filtered(lambda o: o.date_planned < fields.datetime.today()))
        records = self.search([('date_planned','<', fields.datetime.today())])
        print("sea",records)
        for rec in records:
            print("Hellllllllll")
            email_template = self.env.ref('purchase_order_delay_alert.po_delay_mail_template')
            if rec and email_template:
                email_template.send_mail('sidharthpanakool@gmail.com', force_send=True)





        # orders = self.search([
        #     ('date_planned', '<', fields.Date.subtract(fields.date.today(), days=1)),
        #     ('status', '=', 'cancelled')
        # ])
        #         for order in orders:
        #             order.write({'active': False})

        # self.env.user.has_group('purchase.group_purchase_manager')
#         self.env.['res.users'].has_group('purchase.group_purchase_manager')

    # def send_mail(self):
    #     mail_template = self.env.ref('mail.mail_template_test').with_context(lang=self.env.user.lang)
    #     mail_template.send_mail(self.id, force_send=True)

    # def check_for_incomplete_attendances(self):
    #     not_checkout
    #     self.env = ['hr.attendance'].search([('check_out', '=', False)])
    #
    # for rec in not_checkout:
    #
    #     date_time = (datetime.now() + timedelta(days=0))
    #     strftime('% Y-% m-% d 18:29:59')
    #
    #     rec.check_out = date_time
    #
    #     email_template = self.env.ref('custom_attendance_2.email_template')
    #
    #     if email_template:
    #         email_template.send_mail(rec.employee_id.work_email, force_send=True)



