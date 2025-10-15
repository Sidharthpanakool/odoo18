{
    'name': 'Project task limit',
    'version': '18.0.1.0.0',
    'license': "LGPL-3",
    'category': 'Sales',
    'sequence': 1,
    'summary': 'P T L',
    'description': "PTL by SIDHARTH P",
    'author': "ASMI",
    'data': ['views/project_settings_inherit.xml'
             ],
     'assets': {
        'web.assets_backend': [

        ],
        'web.assets_frontend': [

        ]
    },

    'depends': ['base','project'],
    'application': True,
    'auto_install': True,
    'installable': True,
}
