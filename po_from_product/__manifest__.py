{
    'name': 'PO from Product view',
    'version': '18.0.1.0.0',
    'license': "LGPL-3",
    'category': 'Sales',
    'sequence': 1,
    'summary': 'Purchase from the Product view',
    'description': "Purchase order from product view",
    'author': "cybro",
    'data': ["security/ir.model.access.csv",
             "views/product_peoduct_view_inherit.xml",
             "views/wizard_product_product.xml"
             ],
    'assets': {
        'web.assets_backend': [

        ],
        'web.assets_frontend': [

        ]
    },

    'depends': ['base', 'sale', 'sale_management', 'purchase'],
    'application': True,
    'auto_install': True,
    'installable': True,

}
