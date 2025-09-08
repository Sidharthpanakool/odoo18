{
    'name': 'P PAY',
    'version': '18.0.1.0.0',
    'license': "LGPL-3",
    'category': 'Sales/pos',
    'sequence': 1,
    'summary': 'Payment Provider',
    'description': "Payment Provider by SIDHARTH P",
    'author': "ASMI",
    'data': ['data/payment_method.xml',
            'data/payment_provider_record.xml',
             ],
    'assets': {
        'point_of_sale._assets_pos': [

        ],
    },
    'depends': ['base', 'product', 'hr', 'sale', 'sale_management', 'contacts',
                'point_of_sale'],
    'application': True,
    'auto_install': True,
    'installable': True,
}