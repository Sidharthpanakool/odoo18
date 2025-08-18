# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import http
from odoo.http import request


class WebFormController(http.Controller):
    @http.route('/webform', auth='public', website=True)
    def display_web_form(self, **kwargs):
        res_partner = request.env['res.partner'].sudo().search([])
        res_users = request.env['res.users'].sudo().search([])
        vehicle_repair = request.env['vehicle.repair'].sudo().search([])
        vehicle_type = request.env['fleet.vehicle.model.category'].sudo().search([])
        vehicle_model = request.env['fleet.vehicle.model'].sudo().search([])

        data = {'res_partner': res_partner,
                'res_users': res_users,
                'vehicle_model': vehicle_model,
                'vehicle_type': vehicle_type,
                'vehicle_repair': vehicle_repair,
                }
        print('1',  data)
        # print(vehicle_repair)
        return request.render('vehicle_repair_management.web_form_template', data)

    @http.route(['/website/customer/create'], methods=['POST'], type='http', auth='public', website=True, csrf=True)
    def create_customer(self, **post):
        print('kk')
        # print(post.get('name'))
        # print(post.get('mobile_number'))
        # print(post.get('service_advisor_id'))
        # print(post.get('service_type'))
        # print(post.get('vehicle_type'))
        # print(post.get('vehicle_model'))
        # print(post.get('vehicle_number'))
        #
        print('qq', post)
        a = request.env['vehicle.repair'].sudo().create({
            'name': post.get('name'),
            'mobile_number': post.get('mobile_number'),
            'service_advisor_id': post.get('service_advisor_id', False),
            'service_type': post.get('service_type',False),
            'vehicle_type': post.get('vehicle_type',False),
            'vehicle_model': post.get('vehicle_model',False),
            'vehicle_number': post.get('vehicle_number'),
        })
        print('a',a)
        return request.redirect('/contactus-thank-you')


