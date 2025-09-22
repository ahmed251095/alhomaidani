# -*- coding: utf-8 -*-
{'name': "Sale Product/Service Type",
'summary': "Adds a 'نوع المنتجات والخدمات' field to Sale Orders with per-company types and a Sales settings menu to manage them.",
'version': "18.0.1.0.1",
'category': "Sales/Sales",
'author': "ChatGPT (for Ahmed Salah)",
'license': "LGPL-3",
'depends': ["sale_management"],
'data': ["security/sale_service_type_security.xml", "security/ir.model.access.csv", "views/service_type_views.xml", "views/sale_order_views.xml"],
'application': false,
'installable': true}
