# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import  fields, models


class PurchaseOrder(models.Model):
    _inherit = "purchase.order"


    def action_cron_test_po_delayed(self):
        delayed_orders = self.search([('date_planned', '<', fields.Datetime.now()),
                                      ('state', 'in' , ['purchase']),
                                      ('order_line.qty_received', '=' ,0)
                                      ])
        manager_group = self.env.ref('purchase.group_purchase_manager')
        for order in delayed_orders:
            self.env['mail.activity'].create([{
                'res_model_id': self.env['ir.model']._get_id('purchase.order'),
                'res_id': order.id ,
                'activity_type_id': self.env.ref('mail.mail_activity_data_todo').id ,
                'summary': 'Delivery Delayed',
                'note': f'Expected delivery on {order.date_planned.date()} but not received yet.',
                'user_id': order.user_id.id or self.env.user.id,
            }])

            if manager_group:
                order.message_post(
                    body = f"PO {order.name} is delayed. Expected: {order.date_planned.date()}.",
                )











            # for user in manager_group.users:
            #     partner_ids = [user.partner_id.id]









