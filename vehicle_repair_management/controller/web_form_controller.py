from odoo import http
from odoo.http import request


class WebFormController(http.Controller):
    @http.route('/webform', auth='public', website=True)
    def display_web_form(self, **kwargs):
        res_partner=request.env['res.partner'].sudo().search([])
        res_users=request.env['res.users'].sudo().search([])
        vehicle_repair=request.env['vehicle.repair'].sudo().search([])

        vehicle_type = request.env['fleet.vehicle.model.category'].sudo().search([])
        vehicle_model=request.env['fleet.vehicle.model'].sudo().search([])

        # print(vehicle_repair)
        return request.render('vehicle_repair_management.web_form_template',
                              {'res_partner': res_partner,
                               'res_users':res_users.partner_id,
                               'vehicle_model':vehicle_model,
                               'vehicle_type':vehicle_type,
                               'vehicle_repair':vehicle_repair,
                               })

    @http.route('/webform/submit', type='http', auth='public', website=True, methods=['POST'])
    def handle_web_form_submission(self, **post):
        request.env['web.form.vehicle.repair'].sudo().create({
            'name': post.get('name'),
            'mobile_number': post.get('mobile_number'),
            'vehicle_model': post.get('vehicle_model'),
            'vehicle_type': post.get('vehicle_type'),
            'vehicle_number': post.get('vehicle_number'),
            'service_advisor_id': post.get('service_advisor_id'),
            'service_type': post.get('service_type'),

        })
        return request.redirect('/thank-you-page')
