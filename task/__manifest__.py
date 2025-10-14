{
    'name': 'TASK',
    'version': '18.0.1.0.0',
    'license': "LGPL-3",
    'category': 'Sales/crm',
    'sequence': 1,
    'summary': 'TASK',
    'description': "TASK by SIDHARTH P",
    'author': "ASMI",
    'data': ['data/product_template_data.xml',
             'views/view_partner_form.xml',
             ],
     'assets': {
        'web.assets_backend': [

        ],
        'web.assets_frontend': [

        ]
    },

    # 'depends': ['base','mail','sale','sale_management','purchase','contacts','stock','project',],
    'application': True,
    'auto_install': True,
    'installable': True,
}
