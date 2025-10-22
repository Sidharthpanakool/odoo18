{
    'name': 'Production of products',
    'version': '18.0.1.0.0',
    'license': "LGPL-3",
    'category': 'Sales',
    'sequence': 1,
    'summary': 'S o L',
    'description': "Production of Products",
    'author': "Cybro",
    'data': ["security/ir.model.access.csv",
             'views/product_assembly_views.xml',
             'views/product_assemby_menu.xml',
             ],
     'assets': {
        'web.assets_backend': [

        ],
        'web.assets_frontend': [

        ]
    },

    'depends': ['base','stock'],
    'application': True,
    'auto_install': True,
    'installable': True,
}
