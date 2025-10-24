{
    'name': 'Product Manufacturing',
    'version': '18.0.1.0.0',
    'license': "LGPL-3",
    'category': 'Sales',
    'sequence': 1,
    'summary': 'S o L',
    'description': "Manufacturing",
    'author': "Cybro",
    'data': ["security/ir.model.access.csv",
             "views/product_manufacturing_views.xml",
             "views/product_manufacturing_menu.xml",
             ],
    'assets': {
        'web.assets_backend': [

        ],
        'web.assets_frontend': [

        ]
    },

    'depends': ['base','sale_management','stock'],
    'application': True,
    'auto_install': True,
    'installable': True,
}
