{
    'name': 'SO from Customer',
    'version': '18.0.1.0.0',
    'license': "LGPL-3",
    'category': 'Sales',
    'sequence': 1,
    'summary': 'SO from Costomer',
    'description': "Sofc by SIDHARTH P",
    'author': "ASMI",
    'data': ['views/view_partner_form.xml',
             ],
     'assets': {
        'web.assets_backend': [

        ],
        'web.assets_frontend': [

        ]
    },

    'depends': ['base','sale','sale_management','contacts',],
    'application': True,
    'auto_install': True,
    'installable': True,
}
