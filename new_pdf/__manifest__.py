{
  "name": "Sale Quotation Ultra (Standalone)",
  "summary": "Final, conflict-proof standalone quotation report for Odoo 18.",
  "version": "18.0.2.0",
  "category": "Sales",
  "author": "ChatGPT",
  "depends": ["sale_management"],
  "data": [
    "report/report_action.xml",
    "report/quotation_template.xml"
  ],
  "assets": {
    "web.report_assets_common": [
      "sale_quotation_ultra_standalone/static/src/scss/ultra.scss"
    ]
  },
  "license": "LGPL-3",
  "installable": true
}