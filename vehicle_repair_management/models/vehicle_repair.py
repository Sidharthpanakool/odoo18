# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
from email.policy import default

from odoo import api, fields, models, _
from datetime import datetime, timedelta

from odoo.addons.test_convert.tests.test_env import record
from odoo.exceptions import AccessError, UserError, ValidationError

from dateutil.relativedelta import relativedelta


class VehicleRepair(models.Model):
    _name = "vehicle.repair"
    # _rec_name = "reference_number"
    _description = "Vehicle Repair"
    _inherit = ['mail.thread', 'mail.activity.mixin']
    # _order = 'reference_number asc'

    name = fields.Many2one('res.partner',
                           string="Customer",
                           required=True, change_default=True,
                           index=True,
                           tracking=1,
                           check_company=True,
                           )

    reference_number = fields.Char(required=True,
                                   readonly=True, default='New',
                                   copy=False, tracking=True)

    service_advisor_id = fields.Many2one('res.users',
                                         string="Service Advisor", required=True)

    vehicle_type = fields.Many2one('fleet.vehicle.model.category',
                                   string="Vehicle Type")

    vehicle_model = fields.Many2one('fleet.vehicle.model',
                                    string="Vehicle Model",
                                    domain="[('category_id','=',vehicle_type)]"
                                    )

    vehicle_number = fields.Char(string="Vehicle Number",
                                 copy=False, required=True)
    vehicle_image = fields.Binary(string="Vehicle Image",store=True)

    mobile_number = fields.Char(
        comodel_name='res.partner',
        compute='_compute_mobile_number',
        store=True, readonly=False, required=True, precompute=True,
        check_company=True,
        index='btree_not_null',
        string="Mobile Number")

    active = fields.Boolean(default=True)
    invoice_active = fields.Boolean(default=False)
    invoice_paid = fields.Boolean(default=False, compute="_check_payment_status",store=True)
    ribbon_color = fields.Char(compute="_compute_ribbon_color")

    start_date = fields.Date(default=fields.date.today(), required=True)
    duration = fields.Integer(string="Duration(in Days)", required=True)
    delivery_date = fields.Date(string="Delivery Date", compute="_compute_delivery_date",store=True)
    highlight_red = fields.Boolean(compute='_compute_highlight', store=False)
    highlight_yellow = fields.Boolean(compute='_compute_highlight', store=False)

    service_type = fields.Selection(
        string="Service Type",
        selection=[('free', 'Free'), ('paid', 'Paid')],
        required=True
    )
    estimated_amt = fields.Float(string="Estimated Amount")

    status = fields.Selection(
        string="Status",
        tracking=True,
        clickable=True,
        selection=[('draft', 'Draft'), ('progress', 'In Progress'), ('delivery', 'Ready for Deivery'), ('done', 'Done'),
                   ('cancelled', 'cancelled')],
        default="draft"
    )

    repair_tags = fields.Many2many("vehicle.tags", string="Repair Tags")

    company_id = fields.Many2one('res.company', string="Company name", default=lambda self: self.env.company,
                                 readonly=True)

    customer_complaints = fields.Text()

    invoice_id = fields.Many2one('account.move', string="Invoice")

    # service_history_id = fields.Many2one('res.partner', string="Service")
    # print(service_history_id)
    total_sum_sum = fields.Float(string="Total Price", compute="total_sum", store=True)
    labour_cost_sum = fields.Float(string="Total labour cost", compute="total_labour_sum", store=True)

    consumed_parts_ids = fields.One2many('consumed.parts', 'consumed_product_id', "Consumed product")

    labour_cost_ids = fields.One2many('labour.cost', 'labour_cost_id', "Labour cost")

    total_cost = fields.Float(String="Total Cost", compute="_compute_total_cost",store=True)
    @api.depends('total_sum_sum','labour_cost_sum')
    def _compute_total_cost(self):
        """For calculating consumed parts price from the depends total price from consumed parts"""
        for rec in self:
            rec.total_cost = rec.total_sum_sum + rec.labour_cost_sum
            print('total_cost', rec.total_cost)

    _sql_constraints = [
        ('unique_name', 'unique(vehicle_number)', "The vehicle number should be unique.")
    ]

    @api.model
    def action_cron_test_method(self):
        """For checking if any repair form is cancelled and been 1 month,if true,it will archive"""
        print('self', self)
        orders = self.env['vehicle.repair'].search([
            ('start_date', '<', fields.Date.subtract(fields.date.today(), months=1)),
            ('status', '=', 'cancelled')
        ])
        print('orders', orders)
        for order in orders:
            order.write({'active': False})

    @api.model
    def create(self, vals):
        """For the sequence generating here this function is used ,it is the reference number of particular repair service
        here new is the reference number as default,if the reference number is new,it changes to number while saving"""
        if vals.get('reference_number', 'New') == 'New':
            vals['reference_number'] = self.env['ir.sequence'].next_by_code('vehicle.repair.code') or 'New'
        return super(VehicleRepair, self).create(vals)

    @api.onchange('name')
    def num(self):
        """For getting mobile number correspond to the customer by using onchange"""
        if self.name:
            self.mobile_number = self.name.phone

    # def action_wizard_print_report(self):
    #     return {
    #         'name': _('Vehicle Repair Report'),
    #         'view_mode': 'form',
    #         'view_type': 'form',
    #         'res_model': 'wizard.vehicle.repair.report',
    #         'type': 'ir.actions.act_window',
    #         'target': 'new',
    #     }

    def action_confirm(self):
        """For changing the status of the repair,if the button confirm clicks,the status changes to in progress"""
        self.status = "progress"

    def action_confirm_delivery(self):
        """For changing the status of the repair,if the button confirm clicks,the status changes to Ready for delivery"""
        self.status = "delivery"
        template = self.env.ref('vehicle_repair_management.email_template_id')
        template.send_mail(self.id, force_send=True)

    def action_done(self):
        """For changing the status of the repair,if the button confirm clicks,the status changes to done"""
        self.status = "done"

    @api.depends('status','start_date','duration')
    def _compute_delivery_date(self):
        """For calculating estimated delivery date,this function is using timedelta duration is added with start date and calculate delivery date
        """
        today = fields.Date.today()
        for record in self:
            if record.status == 'done':
                record.delivery_date = today
            elif record.start_date and record.duration:
                record.delivery_date = record.start_date + timedelta(days=record.duration)
            else:
                record.delivery_date = record.start_date

    @api.depends('consumed_parts_ids.total_price')
    def total_sum(self):
        """For calculating consumed parts price from the depends total price from consumed parts"""
        for rec in self:
            rec.total_sum_sum = sum(rec.consumed_parts_ids.mapped('total_price'))
            print('total_consumed_parts_price', rec.total_sum)

    @api.depends('labour_cost_ids.sub_total_cost')
    def total_labour_sum(self):
        """For calculating labour cost this function is used
        calculated using the subtotal cost"""
        for rec in self:
            rec.labour_cost_sum = sum(rec.labour_cost_ids.mapped('sub_total_cost'))
            print('total_labour_cost', rec.total_labour_sum)

    def action_create_invoice(self):
        invoice_vals_list = []
        # labour_product = self.env.ref('vehicle_repair_management.product_labour_cost')
        for order in self.labour_cost_ids:
            invoice_vals_list.append((0, 0, {
                'name': f"Labour by {order.user_id.name}",
                'quantity': order.worked_hours,
                'price_unit': order.hourly_cost,

            }))

        for part in self.consumed_parts_ids:
            invoice_vals_list.append((0, 0, {
                'name': f"{part.product_id.name}",
                'quantity': part.product_uom_qty,
                'price_unit': part.list_price,

            }))

        invoice = self.env['account.move'].create({
            'partner_id': self.name.id,
            'move_type': 'out_invoice',
            'invoice_line_ids': invoice_vals_list
        })
        self.invoice_id = invoice.id
        self.write({'invoice_active': True})

        return {
            'type': 'ir.actions.act_window',
            'res_model': 'account.move',
            'res_id': self.invoice_id.id,
            'view_mode': 'form',

        }

    def action_get_invoice_history(self):
        """For fetching invoice history"""
        self.ensure_one()
        return {
            'type': 'ir.actions.act_window',
            'name': 'Service History',
            'view_mode': 'form',
            'res_model': 'account.move',
            'res_id': self.invoice_id.id,
            'target': 'current',

        }

    @api.depends('invoice_id.status_in_payment')
    def _check_payment_status(self):
        for rec in self:
            rec.invoice_paid = rec.invoice_id.status_in_payment == 'paid'

    @api.depends('invoice_paid')
    def _compute_ribbon_color(self):
        for rec in self:
            rec.ribbon_color = 'green' if rec.invoice_paid else 'red'

    @api.depends('status')
    def action_archive(self):
        res = super().action_archive()
        for rec in self:
            if rec.status == 'cancelled':
                rec.active == False
            else:
                rec.active == True
        return res


    @api.depends('status', 'delivery_date')
    def _compute_highlight(self):
        today = fields.Date.today()
        tomorrow = today + timedelta(days=1)
        for rec in self:
            rec.highlight_red = rec.status == 'progress' and rec.delivery_date == today
            rec.highlight_yellow = rec.status == 'progress' and rec.delivery_date == tomorrow

    @api.model
    def status_change(self):
        self.name.write({'customer_status': 'service'})

    # @api.model
    # def status_change(self):
    #     for rec in self.name:
    #         if rec.vehicle_service >= 1:
    #             rec.customer_status = 'service'
    #         else:
    #             rec.customer_status = 'non_service'



