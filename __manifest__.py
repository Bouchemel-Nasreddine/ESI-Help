# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    'name': 'ESI Help',
    'category': 'Administration',
    'description': """
    
""",
    'version': '0.1',
    'depends': [
    ],
    'data': [
        'security/ir.model.access.csv',
        'security/security.xml',
        'views/demande.xml',
        'views/projet.xml',
        'report/report.xml',
        'report/templates.xml',
        'report/templates2.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}
