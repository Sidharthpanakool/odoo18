{
    'name': 'Leave',
    'version': '18.0.1.0.0',
    'license': "LGPL-3",
    'category': 'Human Resources/Attendance',
    'sequence': 1,
    'summary': 'Attendance Module',
    'description': "Daily Attendance By SIDHARTH P",
    'author': "ASMI",
    'data': ["security/ir.model.access.csv",
             "data/ir_cron_data.xml",
             "views/attendance_views.xml",
             "views/attendance_menu.xml"
             ],
    'depends': ['hr','hr_attendance'],
    'application': True,
    'auto_install': True,
    'installable': True,

}