# -*- coding: utf-8 -*-
{
    "name": "Project Task Purchase",
    "version": "18.0.1.0.3",
    "summary": "Create and track Purchase Orders directly from Project Tasks",
    "author": "Ahmed Salah",
    "depends": ["project", "purchase"],
    "data": [
        "views/project_task_views.xml",
        "views/purchase_order_views.xml",
        "security/ir.model.access.csv"
    ],
    "license": "LGPL-3",
    "installable": True,
    "application": False
}
