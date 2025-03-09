{
    'name': "Abimantra : Accounting",
    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",
    'description': """
        Long description of module's purpose
    """,
    'author': "PT Abimantra Sistem Solusindo",
    'website': "https://www.yourcompany.com",
    'category': 'Uncategorized',
    'version': '0.1',
    'depends': ['base',
                'account',],
    'data': [
        'security/ir.model.access.csv',
        'data/sequence.xml',
        'views/branch_views.xml',
        'views/res_users_views.xml',
    ],
    'demo': [
        'demo/demo.xml',
    ],
}
