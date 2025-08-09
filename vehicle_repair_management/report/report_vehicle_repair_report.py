# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
from vobject.base import params_re

from odoo import api, fields, models


class ReportVehicleRepairReport(models.AbstractModel):
    _name = "report.vehicle_repair_management.vehicle_repair_report"

    @api.model
    def _get_report_values(self, docids, data=None):
        print('_get_report_values')

        vehicle_repair_id = tuple(data.get('customer_id'))
        start_date = data.get('start_date')
        end_date = data.get('delivery_date')
        service_advisor =tuple(data.get('service_advisor_id'))
        params = []

        query = """
                    select 
                         pr.name as names,
                        fvmc.name as vehicle_type,
                        vehicle_number,
                        par.name as service_advisor_id,
                        vehicle_repair.start_date,
                        vehicle_repair.delivery_date,
						fvm.name as vehicle_model,
                        status,
                        service_type,
                        estimated_amt,
                        total_cost
                    from
                        vehicle_repair
                    left join res_partner as pr on pr.id=vehicle_repair.name
                    left join res_users as usr on usr.id=vehicle_repair.service_advisor_id                    
                    left join fleet_vehicle_model_category as fvmc on fvmc.id=vehicle_repair.vehicle_type
                    left join res_partner as par on par.id=usr.partner_id 
					left join fleet_vehicle_model as fvm on fvm.id=vehicle_repair.vehicle_model
                    where 
                        usr.active=true
                """

        # if start_date:
        #     query+="""and vehicle_repair.start_date >='%s' """% start_date
        # if end_date:
        #     query+="""and vehicle_repair.start_date <='%s' """% end_date
        if start_date and end_date:
            query += """and vehicle_repair.start_date >='%s' and vehicle_repair.start_date <='%s' """ % (start_date,
                                                                                                         end_date)
        if vehicle_repair_id:
            query += """and vehicle_repair.name in %s """
            params.append(vehicle_repair_id)

        if service_advisor:
            query += """and vehicle_repair.service_advisor_id in %s """
            params.append(service_advisor)

        self.env.cr.execute(query, params)
        report = self.env.cr.dictfetchall()
        print(report)
        return {
            'doc_ids': docids,
            'doc_model': 'vehicle.repair',
            'docs': report,
            'data': data,

        }
