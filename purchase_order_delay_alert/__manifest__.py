{
    'name': 'PO delay create activity',
    'version': '18.0.1.0.0',
    'license': "LGPL-3",
    'category': 'Sales',
    'sequence': 1,
    'summary': 'L o L',
    'description': "PO Activity",
    'author': "ASMI",
    'data': ["data/ir_cron_data.xml",
             "data/mail_template.xml",
             ],
     'assets': {
        'web.assets_backend': [

        ],
        'web.assets_frontend': [

        ]
    },

    'depends': ['base','purchase','contacts'],
    'application': True,
    'auto_install': True,
    'installable': True,
}
