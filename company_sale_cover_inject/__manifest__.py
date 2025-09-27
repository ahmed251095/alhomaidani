# -*- coding: utf-8 -*-
{
    'name': 'Company Sale Cover Inject',
    'version': '1.0',
    'summary': 'Inject cover page into BI Sale Order Report',
    'category': 'Reporting',
    'author': 'Custom',
    'depends': ['sale', 'bi_professional_reports_templates', 'company_sale_report_cover'],
    'data': [
        'views/inject_bi_cover.xml',
    ],
    'installable': True,
    'application': False,
    'license': 'LGPL-3',
}
