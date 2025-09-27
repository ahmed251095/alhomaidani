# -*- coding: utf-8 -*-
{
    'name': 'Sale Order Extra Images',
    'version': '1.0.3',
    'summary': 'Tab on Sale Order to add images; prints them after T&C.',
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
