{
    'name': 'Commission',
    'version': '18.0.1.0.0',
    'license': "LGPL-3",
    'category': 'Sales',
    'sequence': 1,
    'summary': 'Commission',
    'description': "Commission",
    'author': "Cybro",
    'data': ["security/ir.model.access.csv",
             "views/crm_commission_views.xml"
             ],
    'assets': {
        'web.assets_backend': [

        ],
        'web.assets_frontend': [

        ]
    },

    'depends': ['base', 'sale_management'],
    'application': True,
    'auto_install': True,
    'installable': True,
}
