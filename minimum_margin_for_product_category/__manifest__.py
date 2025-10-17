{
    'name': 'Minimum Margin For Product Category',
    'version': '18.0.1.0.0',
    'license': "LGPL-3",
    'category': 'Sales',
    'sequence': 1,
    'summary': 'L o L',
    'description': "Minimum Margin set for the product category,default 15%",
    'author': "Cybro",
    'data': ["views/product_category_inherit_view.xml",
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
