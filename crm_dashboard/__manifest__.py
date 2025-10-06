{
    'name': 'CRM Dashboard',
    'version': '18.0.1.0.0',
    'license': "LGPL-3",
    'category': 'Sales/crm',
    'sequence': 1,
    'summary': 'CRM Dashboard',
    'description': "Crm Dashboard SIDHARTH P",
    'author': "ASMI",
    'data': ['views/ir_actions_views.xml',
             'views/inherit.xml',
             ],
     'assets': {
        'web.assets_backend': [
            'crm_dashboard/static/src/js/dashboard.js',
            'crm_dashboard/static/src/xml/dashboard.xml',
            'crm_dashboard/static/src/xml/kpi_card.xml',
        ],
        'web.assets_frontend': [

        ]
    },

    'depends': ['base','mail','sale','crm'],
    'application': True,
    'auto_install': True,
    'installable': True,
}
