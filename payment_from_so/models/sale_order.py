# -*- coding: utf-8 -*-
from odoo import models
from odoo.exceptions import UserError

class SaleOrder(models.Model):
    _inherit = 'sale.order'

    def action_payment_direct_from_so(self):
        if not self.order_line:
            raise UserError("Cannot create invoice for a sale order with no order lines.")

        invoice_creation = self.env['sale.advance.payment.inv'].with_context(active_model="sale.order", active_ids=self.ids).create([{
            'advance_payment_method': 'delivered'
            }])
        if not self.invoice_ids:
            created_inv = invoice_creation.create_invoices()
        if self.invoice_ids:
            created_inv = self.invoice_ids

        created_inv.filtered(lambda inv: inv.state == 'draft').action_post()
        payment = (
            self.env['account.payment.register']
            .with_context(active_model='account.move',
                          active_ids= created_inv.ids,
                          default_amount= created_inv.amount_total,
                          default_partner_id= created_inv.id,
                          ).create({
                'amount': created_inv.amount_total,
                'communication': created_inv.name,
                'partner_id': created_inv.partner_id.id,
            })
        )
        payment.action_create_payments()