# -*- coding: utf-8 -*-
{
    'name': 'Sale Order Extra Images',
    'version': '1.0.0',
    'summary': 'Add a tab on Sale Order to attach images and print them after Terms & Conditions.',
    'category': 'Sales/Reporting',
    'author': 'Custom',
    'depends': ['sale', 'bi_professional_reports_templates'],
    'data': [
        'security/ir.model.access.csv',
        'views/sale_order_views.xml',
        'views/report_inherit.xml',
    ],
    'license': 'LGPL-3',
    'installable': True,
    'application': False,
}
