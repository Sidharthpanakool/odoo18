# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
from odoo import api, fields, models


class ReportVehicleRepairReport(models.AbstractModel):
    _name = "report.vehicle_repair_management.vehicle_repair_report"

    @api.model
    def _get_report_values(self, docids, data=None):
        print('_get_report_values')
        query = """
                    select
                        pr.name as name,
                        fvmc.name as vehicle_model,
                        vehicle_number,
                        par.name as service_advisor_id,
                        start_date,
                        delivery_date,
                        status,
                        fvm.name as vehicle_type,
                        service_type,
                        estimated_amt,
                        total_cost
                    from
                        vehicle_repair
                    left join res_partner as pr on pr.id=vehicle_repair.name
                    left join res_users as usr on usr.id=vehicle_repair.service_advisor_id                    
                    left join fleet_vehicle_model as fvm on fvm.category_id=vehicle_repair.vehicle_type
                    left join fleet_vehicle_model_category as fvmc on fvmc.sequence=vehicle_repair.vehicle_model
                    left join res_partner as par on par.id=usr.partner_id 
                    
                    where usr.active=true 
                    
                """
        # # if self.from_date:
        # #     query += """ where tb.date >= '%s' and tb.date <= '%s'""" % self.from_date, %self.to_date
        # self.env.cr.execute(query)
        self.env.cr.execute(query)
        report = self.env.cr.dictfetchall()
        # report = self.env['action_report_vehicle_repair']._get_report_from_name('module.vehicle_repair_management_vehicle_repair_report')

        docs = self.env['wizard.vehicle.repair.report'].browse(docids)
        print(docs)
        return {
            'doc_ids': docids,
            'doc_model': 'vehicle.repair',
            'docs': report,
            'data': data,

        }
