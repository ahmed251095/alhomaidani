{
    "name": "Sale Quotation Ultra",
    "summary": "Premium quotation for Odoo 18 – robust xpaths, no 'o' in attrs, RTL via :lang(ar).",
    "version": "18.0.1.2",
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