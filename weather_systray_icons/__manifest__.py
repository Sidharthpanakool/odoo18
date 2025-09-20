{
    'name': 'Weather Systray Icon',
    'version': '18.0.1.0.0',
    'license': "LGPL-3",
    'category': 'Sales/weather',
    'sequence': 1,
    'summary': 'Weather Systray Icon',
    'description': "Weather Systray Icon by SIDHARTH P",
    'author': "ASMI",
    'data': [
             ],
    'assets': {
        'web.assets_backend': [
            'weather_systray_icons/static/src/js/systray.js',
            'weather_systray_icons/static/src/xml/systray_templates.xml',
        ],
        'web.assets_frontend': [

        ]
    },

    'depends': ['base','mail'],
    'application': True,
    'auto_install': True,
    'installable': True,

}
