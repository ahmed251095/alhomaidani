# -*- coding: utf-8 -*-
{
    "name": "Customer/Vendor Filter in Quotations and Purchase Orders",
    "summary": "Show only customers in quotations and only vendors in purchase orders",
    "version": "18.0.2.0.0",
    "author": "Ahmed's Assistant",
    "website": "https://example.com",
    "license": "LGPL-3",
    "category": "Sales/Purchase",
    "depends": ["sale", "purchase"],
    "data": [
        "views/sale_order_view.xml",
        "views/purchase_order_view.xml",
    ],
    "installable": True,
    "application": False,
}