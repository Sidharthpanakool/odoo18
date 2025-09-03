{
    'name': 'POS Storage Location',
    'version': '18.0.1.0.0',
    'license': "LGPL-3",
    'category': 'Sales/pos',
    'sequence': 1,
    'summary': 'product Storage Location',
    'description': "pos update SIDHARTH P",
    'author': "ASMI",
    'data': [
            'views/pos_configuration_settings_form.xml',
             ],
    'assets': {
        'point_of_sale._assets_pos': [
            "pos_storage_location/static/src/**/*",
        ],
    },
    'depends': ['base', 'product', 'hr', 'sale', 'sale_management', 'contacts',
                'point_of_sale'],
    'application': True,
    'auto_install': True,
    'installable': True,
}
