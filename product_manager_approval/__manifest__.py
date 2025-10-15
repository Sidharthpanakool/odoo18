{
    'name': 'Product Approval by Manager',
    'version': '18.0.1.0.0',
    'license': "LGPL-3",
    'category': 'Sales',
    'sequence': 1,
    'summary': 'L o L',
    'description': "Product Approval",
    'author': "Cybro",
    'data': ['security/product_access_groups.xml',
             'security/ir.model.access.csv',
             'views/request_form_view.xml'
             ],
     'assets': {
        'web.assets_backend': [

        ],
        'web.assets_frontend': [

        ]
    },

    'depends': ['base','purchase','sale'],
    'application': True,
    'auto_install': True,
    'installable': True,
}
