# -*- coding: utf-8 -*-
{
    'name': 'Sale Order Extra HTML',
    'version': '1.0.0',
    'summary': 'Add an HTML tab on Sale Orders and print it after Terms & Conditions.',
    'category': 'Sales/Reporting',
    'author': 'Custom',
    'depends': ['sale', 'bi_professional_reports_templates'],
    'data': [
        'views/sale_order_views.xml',
        'views/fix_remove_tcall.xml',
        'views/report_inherit.xml',
        'security/ir.model.access.csv',
    ],
    'license': 'LGPL-3',
    'installable': True,
    'application': False,
}
