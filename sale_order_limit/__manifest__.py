{
    'name': 'Sale Order Limit',
    'version': '18.0.1.0.0',
    'license': "LGPL-3",
    'category': 'Sales',
    'sequence': 1,
    'summary': 'S o L',
    'description': "SO Maximum amount set in settings",
    'author': "Cybro",
    'data': ['views/res_config_settings_view.xml'
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
