{
    'name': 'VIP Discount',
    'version': '18.0.1.0.0',
    'license': "LGPL-3",
    'category': 'Sales',
    'sequence': 1,
    'summary': 'L o L',
    'description': "Discount for vip customer",
    'author': "ASMI",
    'data': ['views/res_partner_form_view.xml',
             ],
     'assets': {
        'web.assets_backend': [

        ],
        'web.assets_frontend': [

        ]
    },

    'depends': ['base','sale','sale_management'],
    'application': True,
    'auto_install': True,
    'installable': True,
}
