{
    'name': 'POS Product Owner',
    'version': '18.0.1.0.0',
    'license': "LGPL-3",
    'category': 'Sales/pos',
    'sequence': 1,
    'summary': 'product owner',
    'description': "pos update SIDHARTH P",
    'author': "ASMI",
    'data': ['views/product_owner_pos.xml',
             ],
    'assets': {
        'point_of_sale._assets_pos': [
            "pos_product_owner/static/src/**/*",
        ],
        'web.assets_backend': [

        ],
        'web.assets_frontend': [

        ]
    },

    'depends': ['base', 'hr', 'sale', 'contacts',
                'point_of_sale'],
    'application': True,
    'auto_install': True,
    'installable': True,

}