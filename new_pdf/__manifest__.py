{
    "name": "Sale Quotation Ultra",
    "summary": "Premium, compact, Arabic-friendly quotation print for Odoo 18 (no empty gaps, stunning header, clean totals).",
    "version": "18.0.1.0",
    "category": "Sales",
    "author": "ChatGPT",
    "depends": ["sale_management"],
    "data": [
        "report/report_action.xml",
        "report/quotation_template.xml"
    ],
    "assets": {
        "web.report_assets_common": [
            "sale_quotation_ultra/static/src/scss/ultra.scss"
        ]
    },
    "license": "LGPL-3",
    "installable": True,
    "application": False
}