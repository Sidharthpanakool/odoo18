# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
from odoo import http
from odoo.http import request

class SnippetController(http.Controller):
    @http.route('/get_top_vehicles', auth="public", type='json',
                website=True)
    def get_top_vehicle(self):
        orders = (request.env['vehicle.repair'].sudo().search_read
                    (
                    [('active', '=', True)],
                    fields=['id','partner_id',
                            'reference_number',
                            'mobile_number',
                            'service_advisor_id',
                            'vehicle_number',
                            'vehicle_image',
                            'vehicle_type',
                            'vehicle_model'],
                            order='id desc',
                            limit=4
                    )
                )
        values = {
            'vehicles': orders,
        }
        return values
