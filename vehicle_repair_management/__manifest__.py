{
    'name': 'vehicle_repair_management',
    'version': '18.0.1.2.0',
    'license': "LGPL-3",
    'category': 'Sales/Vehicle',
    'sequence': 1,
    'summary': 'Vehicle Repair Management Application For Vehicle Repair',
    'description': "VRM SIDHARTH P",
    'author': "ASMI",
    'data': ["security/user_groups.xml",
             "security/user_groups_access.xml",
             "security/ir.model.access.csv",
             "data/ir_cron_data.xml",
             "data/product_data.xml",
             "data/email_template.xml",
             "data/vehicle_type_data.xml",
             "data/ir_module_category_data.xml",
             "data/ir_action_server.xml",
             "data/web_form_template.xml",
             "views/vehicle_repair_views.xml",
             "views/res_partner_views.xml",
             "views/snippets/top_four_vehicle.xml",
             "report/ir_actions_report.xml",
             "report/vehicle_repair_report.xml",
             "wizard/wizard_vehicle_repair_report_views.xml",
             "views/vehicle_repair_menu.xml",
             ],
    'assets': {
        'web.assets_backend': [
            'vehicle_repair_management/static/src/js/action_manager.js',
        ],
        'web.assets_frontend': [
            'vehicle_repair_management/static/src/js/snippet.js',
            'vehicle_repair_management/static/src/xml/top_vehicle_snippet_owl.xml',
        ]
    },

    'depends': ['base', 'fleet', 'product', 'sale', 'hr', 'account', 'mail', 'sale_management', 'contacts', 'website',
                'base_automation'],
    'application': True,
    'auto_install': True,
    'installable': True,

}
