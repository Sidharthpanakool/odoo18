{
    'name': 'Sale Order In Invoice',
    'version': '18.0.1.0.0',
    'license': "LGPL-3",
    'category': 'Sales',
    'sequence': 1,
    'summary': 'S o L',
    'description': "SO in invoice",
    'author': "Cybro",
    'data': ['views/account_view_move_form.xml'
             ],
     'assets': {
        'web.assets_backend': [

        ],
        'web.assets_frontend': [

        ]
    },

    'depends': ['base','sale','account','sale_management'],
    'application': True,
    'auto_install': True,
    'installable': True,
}
