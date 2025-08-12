# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
from vobject.base import params_re
import io
import json
import xlsxwriter
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
                    left join res_partner as pr on pr.id=vehicle_repair.name
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
                        vehicle_repair.active=true 
                        and usr.active=true
                """
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

        output = io.BytesIO()
        workbook = xlsxwriter.Workbook(output, {'in_memory': True})
        sheet = workbook.add_worksheet()
        cell_format = workbook.add_format(
            {'font_size': '11px', 'align': 'left', 'bold': True, })
        head = workbook.add_format(
            {'align': 'center', 'bold': True, 'font_size': '25px'})
        txt = workbook.add_format({'font_size': '10px', 'align': 'left'})

        date_style = workbook.add_format({'num_format': 'dd-mm-yyyy'})
        sheet.merge_range('B2:V3', 'VEHICLE REPAIR REPORT', head)

        if not length_vehicle_repair_id == 1:
            sheet.write('A7', 'customer', cell_format)
        sheet.write('B7', 'Vehicle Model', cell_format)
        sheet.write('C7', 'Vehicle Number', cell_format)

        if not length_service_advisor == 1:
            sheet.write('D7', 'Service Advisor', cell_format)
        sheet.write('E7', 'Start Date', date_style)
        sheet.write('F7', 'End Date', date_style)
        sheet.write('G7', 'State', cell_format)
        sheet.write('H7', 'Vehicle Type', cell_format)
        sheet.write('I7', 'Service Type', cell_format)
        sheet.write('J7', 'Estimated Amount', cell_format)
        sheet.write('K7', 'Total Amount', cell_format)
        i = 7

        for record in report:
            i += 1
            print("count:", i)
            if length_vehicle_repair_id == 1:
                sheet.write('A4', 'Customer:', cell_format)
                sheet.write('B4', record['names'], txt)

            if length_service_advisor == 1:
                sheet.write('A5', '   Advisor:', cell_format)
                sheet.write('B5', record['service_advisor_id'], txt)
            if not length_vehicle_repair_id == 1:
                sheet.write(f'A{i}', record['names'], txt)

            sheet.write(f'B{i}', record['vehicle_model'], txt)
            sheet.write(f'C{i}', record['vehicle_number'], txt)

            if not length_service_advisor == 1:
                sheet.write(f'D{i}', record['service_advisor_id'], txt)

            sheet.write(f'E{i}', record['start_date'], date_style)
            sheet.write(f'F{i}', record['delivery_date'], date_style)
            sheet.write(f'G{i}', record['status'], txt)
            sheet.write(f'H{i}', record['vehicle_type'], txt)
            sheet.write(f'I{i}', record['service_type'], txt)
            sheet.write(f'J{i}', record['estimated_amt'], txt)
            sheet.write(f'K{i}', record['total_cost'], txt)

        workbook.close()
        output.seek(0)
        response.stream.write(output.read())
        output.close()

