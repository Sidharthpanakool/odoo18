{
    'name': 'Quiz Idle Timer',
    'version': '18.0.1.0.0',
    'license': "LGPL-3",
    'category': 'Survey/Quiz Idle Timer',
    'sequence': 1,
    'summary': 'Quiz Idle Timer',
    'description': "Quiz Idle Timer by SIDHARTH P",
    'author': "ASMI",

    'data': ['views/survey_survey_form.xml',
             'views/survey_session_template.xml'
             ],

    'assets': {
        'survey.survey_assets': [
            'quiz_idle_timer/static/src/js/quiz_idle_timer.js'
        ],
        'web.assets_backend': [

        ],
        'web.assets_frontend': [

        ]
    },

    'depends': ['base', 'mail', 'survey'],
    'application': True,
    'auto_install': True,
    'installable': True,

}
