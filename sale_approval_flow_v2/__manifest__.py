# -*- coding: utf-8 -*-
{
    "name": "Sale: Quotation Multi-Stage Approval (L1/L2 + Reject)",
    "summary": "Salesman submits; Level1 approves then Level2 approves; reject with reason; block confirm until fully approved.",
    "version": "18.0.2.10",
    "author": "ChatGPT",
    "depends": ["sale_management", "mail"],
    "data": [
        "security/sale_approval_security.xml",
        "security/ir.model.access.csv",
        "views/sale_order_views.xml"
    ],
    "application": False,
    "installable": True,
    "license": "LGPL-3",
}