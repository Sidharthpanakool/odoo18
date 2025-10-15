# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
from odoo import fields, models, api
from odoo.exceptions import ValidationError


class PurchaseOrder(models.Model):
    _inherit = "purchase.order"

    restricted_boolean = fields.Boolean("Restricted", related='partner_id.restricted')
    restricted_count = fields.Integer(string='Order line limit',related='partner_id.restricted_count')

    sale_count_confirmed = fields.Integer(string="Sale order count", compute="_compute_sale_count_confirmed" )

    @api.depends('partner_id.sale_order_ids')
    def _compute_sale_count_confirmed(self):
        for rec in self:
            sale = self.env['sale.order'].search_count([('state','=','sale'),('partner_id','=',rec.partner_id.id)])
            rec.sale_count_confirmed = sale
            print(sale)


    def button_confirm(self):
        if self.restricted_boolean and self.restricted_count < len(self.order_line):
            raise ValidationError('Your Order Line Limit Exceeded')
        return super().button_confirm()




class DemoModel(models.Model):
    _name="demo.model"

    user=fields.Char()

    @api.constrains('user')
    def _unic_model(self,user):
        record = self.browse(user)
        if record.exists():
            raise ValidationError('Already Exists')


    _sql_constraints = [('user', 'unique(user)', "The user name must be unique!")]








        # for order in self:
        #     restricted_partner = self.env['res.partner'].search([('id', '=', order.partner_id.id)], )
        #     print(restricted_partner.restricted)
        #     print(restricted_partner.restricted_count)
        #     if restricted_partner and restricted_partner.restricted == True:
        #         vals['restricted_boolean'] = True
        #         vals['restricted_count'] = restricted_partner.restricted_count
        #     else:
        #         vals['restricted_boolean'] = False
        #
        # return super(PurchaseOrder, self).write(vals)


    # def write(self, vals):
    #     for order in self:
    #         restricted_partner = self.env['res.partner'].search([('id', '=', order.partner_id.id)], )
    #         print(restricted_partner.restricted)
    #         print(restricted_partner.restricted_count)
    #         if restricted_partner and restricted_partner.restricted == True:
    #             vals['restricted_boolean'] = True
    #             vals['restricted_count'] = restricted_partner.restricted_count
    #         else:
    #             vals['restricted_boolean'] = False
    #
    #     return super(PurchaseOrder, self).write(vals)

    # def button_confirm(self):
    #     restricted_partner = self.env['res.partner'].search([('id', '=', self.partner_id.id)])
    #     purchase_order_line = self.env['purchase.order.line'].search_count([('order_id', '=', self.id)])
    #     print(purchase_order_line)
    #     if restricted_partner.restricted and purchase_order_line > self.restricted_count:
    #         raise ValidationError('Your Limit Exceeded')
    #
    #     return super().button_confirm()

    # def button_confirm(self):
    #     today=fields.Date.today()
    #     res =  super().button_confirm()
    #     partner=self.env['res.partner'].search([('id','=',self.partner_id.id)])
    #     print('partner',partner.id)
    #
    #     confirm_date = self.search_read([('id','=',self.partner_id.id)], ['date_approve'],)
    #     if confirm_date:
    #         confirm_date=confirm_date[0]
    #         confirm_date=confirm_date['date_approve']
    #         print('c', confirm_date)
    #         print('t',today)
    #
    #         if partner:
    #             for rec in partner:
    #                 rec.last_reference_date=today
    #                 # if confirm_date:
    #                 date_difference=(today-confirm_date.date()).days
    #                 print('date_difference',date_difference)
    #                 if date_difference>1:
    #                     raise ValidationError('Sorry Cant confirm')
    #             else:
    #                 return res













