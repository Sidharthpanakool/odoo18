# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
from vobject.base import params_re
import io
import json
import xlsxwriter
from xlsxwriter import worksheet

from odoo import models
from odoo.tools import json_default
from odoo import api, fields, models
from odoo.addons.test_convert.tests.test_env import record


class ReportVehicleRepairReport(models.AbstractModel):
    _name = "report.vehicle_repair_management.vehicle_repair_report"

    @api.model
    def _get_report_values(self, docids, data=None):
        print('_get_report_values')

        vehicle_repair_id = tuple(data.get('customer_id'))
        start_date = data.get('start_date')
        end_date = data.get('delivery_date')
        service_advisor = tuple(data.get('service_advisor_id'))

        length_service_advisor = (len(service_advisor))
        length_vehicle_repair_id = (len(vehicle_repair_id))

        print(length_service_advisor)
        print(length_vehicle_repair_id)

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
                    left join res_partner as pr on pr.id=vehicle_repair.partner_id
                    left join res_users as usr on usr.id=vehicle_repair.service_advisor_id                    
                    left join fleet_vehicle_model_category as fvmc on fvmc.id=vehicle_repair.vehicle_type
                    left join res_partner as par on par.id=usr.partner_id 
					left join fleet_vehicle_model as fvm on fvm.id=vehicle_repair.vehicle_model
                    where 
                        vehicle_repair.active=true 
                        and usr.active=true
                """
        if start_date  and end_date:
            query += """and vehicle_repair.start_date >='%s' and vehicle_repair.start_date <='%s' """ % (start_date,end_date)


        if vehicle_repair_id:
            query += """and vehicle_repair.partner_id in %s """
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
            'length_vehicle_repair_id': length_vehicle_repair_id,
            'length_service_advisor': length_service_advisor,
        }

    def get_xlsx_report(self, data, response):
        print("get_xlsx_report")

        vehicle_repair_id = tuple(data.get('customer_id'))
        start_date = data.get('start_date')
        end_date = data.get('delivery_date')
        service_advisor = tuple(data.get('service_advisor_id'))

        length_service_advisor = (len(service_advisor))
        length_vehicle_repair_id = (len(vehicle_repair_id))

        print(length_service_advisor)
        print(length_vehicle_repair_id)

        params = []

        query = """
                    select 
                         pr.name as names,
                        fvmc.name as vehicle_type,
                        vehicle_number,
                        par.name as service_advisor_id,
                        start_date,
                        delivery_date,
                        fvm.name as vehicle_model,
                        status,
                        service_type,
                        estimated_amt,
                        total_cost
                    from
                        vehicle_repair
                    left join res_partner as pr on pr.id=vehicle_repair.partner_id
                    left join res_users as usr on usr.id=vehicle_repair.service_advisor_id                    
                    left join fleet_vehicle_model_category as fvmc on fvmc.id=vehicle_repair.vehicle_type
                    left join res_partner as par on par.id=usr.partner_id 
                    left join fleet_vehicle_model as fvm on fvm.id=vehicle_repair.vehicle_model
                    where 
                        vehicle_repair.active=true 
                        and usr.active=true
                """
        if start_date and end_date:
            query += """and vehicle_repair.start_date >='%s' and vehicle_repair.start_date <='%s' """ % (start_date,
                                                                                                         end_date)
        if vehicle_repair_id:
            query += """and vehicle_repair.partner_id in %s """
            params.append(vehicle_repair_id)

        if service_advisor:
            query += """and vehicle_repair.service_advisor_id in %s """
            params.append(service_advisor)

        self.env.cr.execute(query, params)
        report = self.env.cr.dictfetchall()

        output = io.BytesIO()
        workbook = xlsxwriter.Workbook(output, {'in_memory': True})
        sheet = workbook.add_worksheet()
        cell_format = workbook.add_format(
            {'font_size': '11px', 'align': 'center', 'bold': True,
             'font_color': 'white',
             'bg_color': 'black'})
        head = workbook.add_format(
            {'align': 'center', 'bold': True, 'font_size': '25px',
             'font_color': 'red',
             'bg_color': 'black'
             })
        txt = workbook.add_format({'font_size': '10px', 'align': 'center'})
        date_style = workbook.add_format({'num_format': 'dd-mm-yyyy', 'align': 'center', })

        sheet.set_column(0, 10, 17.5)
        sheet.set_row(8, 30)

        if length_vehicle_repair_id == 1 and not length_service_advisor == 1:
            sheet.merge_range(1, 1, 3, 8, 'VEHICLE REPAIR REPORT', head)
        if length_service_advisor == 1 and not length_vehicle_repair_id == 1:
            sheet.merge_range(1, 1, 3, 8, 'VEHICLE REPAIR REPORT', head)
        if length_vehicle_repair_id == 1 and length_service_advisor == 1:
            sheet.merge_range(1, 1, 3, 7, 'VEHICLE REPAIR REPORT', head)
        if not length_vehicle_repair_id == 1 and not length_service_advisor == 1:
            sheet.merge_range(1, 1, 3, 9, 'VEHICLE REPAIR REPORT', head)
        total_cost=[]
        est_amt=[]
        i = 9
        for record in report:
            i += 1
            print("count:", i)
            if length_vehicle_repair_id == 1 and not length_service_advisor == 1:

                sheet.write(5, 0, 'Customer:', cell_format)
                sheet.write(5, 1, record['names'], txt)
                sheet.set_row(5, 25)

                sheet.write(8, 0, 'Vehicle Model', cell_format)
                sheet.write(8, 1, 'Vehicle Number', cell_format)
                sheet.write(8, 2, 'Service Advisor', cell_format)
                sheet.write(8, 3, 'Start Date', cell_format)
                sheet.write(8, 4, 'End Date', cell_format)
                sheet.write(8, 5, 'State', cell_format)
                sheet.write(8, 6, 'Vehicle Type', cell_format)
                sheet.write(8, 7, 'Service Type', cell_format)
                sheet.write(8, 8, 'Estimated Amount', cell_format)
                sheet.write(8, 9, 'Total Amount', cell_format)

                sheet.write(i - 1, 0, record['vehicle_model'], txt)
                sheet.write(i - 1, 1, record['vehicle_number'], txt)
                sheet.write(i - 1, 2, record['service_advisor_id'], txt)
                sheet.write(i - 1, 3, record['start_date'], date_style)
                sheet.write(i - 1, 4, record['delivery_date'], date_style)
                sheet.write(i - 1, 5, record['status'], txt)
                sheet.write(i - 1, 6, record['vehicle_type'], txt)
                sheet.write(i - 1, 7, record['service_type'], txt)
                sheet.write(i - 1, 8, record['estimated_amt'], txt)
                sheet.write(i - 1, 9, record['total_cost'], txt)

            if length_service_advisor == 1 and not length_vehicle_repair_id == 1:

                sheet.write(6, 0, '   Advisor:', cell_format)
                sheet.write(6, 1, record['service_advisor_id'], txt)
                sheet.set_row(6, 25)

                sheet.write(8, 0, 'customer', cell_format)
                sheet.write(8, 1, 'Vehicle Model', cell_format)
                sheet.write(8, 2, 'Vehicle Number', cell_format)
                sheet.write(8, 3, 'Start Date', cell_format)
                sheet.write(8, 4, 'End Date', cell_format)
                sheet.write(8, 5, 'State', cell_format)
                sheet.write(8, 6, 'Vehicle Type', cell_format)
                sheet.write(8, 7, 'Service Type', cell_format)
                sheet.write(8, 8, 'Estimated Amount', cell_format)
                sheet.write(8, 9, 'Total Amount', cell_format)

                sheet.write(i - 1, 0, record['names'], txt)
                sheet.write(i - 1, 1, record['vehicle_model'], txt)
                sheet.write(i - 1, 2, record['vehicle_number'], txt)
                sheet.write(i - 1, 3, record['start_date'], date_style)
                sheet.write(i - 1, 4, record['delivery_date'], date_style)
                sheet.write(i - 1, 5, record['status'], txt)
                sheet.write(i - 1, 6, record['vehicle_type'], txt)
                sheet.write(i - 1, 7, record['service_type'], txt)
                sheet.write(i - 1, 8, record['estimated_amt'], txt)
                sheet.write(i - 1, 9, record['total_cost'], txt)

            if length_vehicle_repair_id == 1 and length_service_advisor == 1:

                sheet.write(5, 0, 'Customer:', cell_format)
                sheet.write(5, 1, record['names'], txt)
                sheet.set_row(5, 25)

                sheet.write(6, 0, '   Advisor:', cell_format)
                sheet.write(6, 1, record['service_advisor_id'], txt)
                sheet.set_row(6, 25)

                sheet.write(8, 0, 'Vehicle Model', cell_format)
                sheet.write(8, 1, 'Vehicle Number', cell_format)
                sheet.write(8, 2, 'Start Date', cell_format)
                sheet.write(8, 3, 'End Date', cell_format)
                sheet.write(8, 4, 'State', cell_format)
                sheet.write(8, 5, 'Vehicle Type', cell_format)
                sheet.write(8, 6, 'Service Type', cell_format)
                sheet.write(8, 7, 'Estimated Amount', cell_format)
                sheet.write(8, 8, 'Total Amount', cell_format)

                sheet.write(i - 1, 0, record['vehicle_model'], txt)
                sheet.write(i - 1, 1, record['vehicle_number'], txt)
                sheet.write(i - 1, 2, record['start_date'], date_style)
                sheet.write(i - 1, 3, record['delivery_date'], date_style)
                sheet.write(i - 1, 4, record['status'], txt)
                sheet.write(i - 1, 5, record['vehicle_type'], txt)
                sheet.write(i - 1, 6, record['service_type'], txt)
                sheet.write(i - 1, 7, record['estimated_amt'], txt)
                sheet.write(i - 1, 8, record['total_cost'], txt)

            if not length_vehicle_repair_id == 1 and not length_service_advisor == 1:

                sheet.write(8, 0, 'customer', cell_format)
                sheet.write(8, 1, 'Vehicle Model', cell_format)
                sheet.write(8, 2, 'Vehicle Number', cell_format)
                sheet.write(8, 3, 'Service Advisor', cell_format)
                sheet.write(8, 4, 'Start Date', cell_format)
                sheet.write(8, 5, 'End Date', cell_format)
                sheet.write(8, 6, 'State', cell_format)
                sheet.write(8, 7, 'Vehicle Type', cell_format)
                sheet.write(8, 8, 'Service Type', cell_format)
                sheet.write(8, 9, 'Estimated Amount', cell_format)
                sheet.write(8, 10, 'Total Amount', cell_format)

                sheet.write(i - 1, 0, record['names'], txt)
                sheet.write(i - 1, 1, record['vehicle_model'], txt)
                sheet.write(i - 1, 2, record['vehicle_number'], txt)
                sheet.write(i - 1, 3, record['service_advisor_id'], txt)
                sheet.write(i - 1, 4, record['start_date'], date_style)
                sheet.write(i - 1, 5, record['delivery_date'], date_style)
                sheet.write(i - 1, 6, record['status'], txt)
                sheet.write(i - 1, 7, record['vehicle_type'], txt)
                sheet.write(i - 1, 8, record['service_type'], txt)
                sheet.write(i - 1, 9, record['estimated_amt'], txt)
                sheet.write(i - 1, 10, record['total_cost'], txt)

            total_cost.append(record['total_cost'])
            est_amt.append(record['estimated_amt'])
        est=sum(est_amt)
        print("EST",est)
        sum_o=sum(total_cost)
        print(sum_o,"sum")
        workbook.close()
        output.seek(0)
        response.stream.write(output.read())
        output.close()
