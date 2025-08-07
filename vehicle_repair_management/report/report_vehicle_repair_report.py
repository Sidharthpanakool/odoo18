# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
from odoo import api, fields, models


class ReportVehicleRepairReport(models.AbstractModel):
    _name = "report.vehicle_repair.vehicle_repair_report"

    @api.model
    def _get_report_values(self, docids, data=None):
        print('_get_report_values')
        start = data.get('start_date')
        query = """
                        select
                            pr.name,
                            vehicle_model,
                            vehicle_number,
                            service_advisor_id,
                            start_date,
                            status,
                            vehicle_type,
                            service_type,
                            estimated_amt
                        from
                            vehicle_repair
                        left join res_partner as pr on pr.id=vehicle_repair.name;
                        """
        # # if self.from_date:
        # #     query += """ where tb.date >= '%s' and tb.date <= '%s'""" % self.from_date, %self.to_date
        # self.env.cr.execute(query)
        self.env.cr.execute(query)
        report = self.env.cr.dictfetchall()

        docs = self.env['wizard.vehicle.repair.report'].browse(docids)
        print(docs)
        return {
            'doc_ids': docids,
            'doc_model': 'vehicle.repair',
            'docs': report,
            'data': data,

        }
