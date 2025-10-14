{
    'name': 'line order limit',
    'version': '18.0.1.0.0',
    'license': "LGPL-3",
    'category': 'Sales',
    'sequence': 1,
    'summary': 'L o L',
    'description': "LoL by SIDHARTH P",
    'author': "ASMI",
    'data': [ 'views/view_partner_form.xml',
             ],
     'assets': {
        'web.assets_backend': [

        ],
        'web.assets_frontend': [

        ]
    },

    'depends': ['base','purchase','contacts',],
    'application': True,
    'auto_install': True,
    'installable': True,
}
