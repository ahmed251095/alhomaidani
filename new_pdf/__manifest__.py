{
    "name": "Sale Quotation Ultra",
    "summary": "Premium quotation print for Odoo 18 – safer XPaths (insert-only), Arabic-friendly, zero dead space.",
    "version": "18.0.1.1",
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
    "license": "LGPL-3"
}