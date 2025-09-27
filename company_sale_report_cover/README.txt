Company Sale Report Cover
=========================

This module adds two fields on `res.company`:
- `sale_report_cover` (Binary image)
- `sale_report_cover_fit` (object-fit behavior)

It **does not** modify any report automatically.
Include the following reusable QWeb template snippet into your report to show the company-specific cover page as the first page.

Example usage inside your report:
---------------------------------
Place this block **inside** your report template (usually right after `<t t-call="web.external_layout">`),
and **before** your normal content pages:

    <!-- Cover page -->
    <div class="page" style="direction: rtl; text-align: center; padding:0; margin:0;">
      <t t-if="doc.company_id.sale_report_cover">
        <img t-att-src="'/web/image/res.company/%s/sale_report_cover' % doc.company_id.id"
             t-att-style="'width:100%; height:100%; object-fit:%s; display:block; margin:0;'" 
             t-attf-style="'object-fit: #{doc.company_id.sale_report_cover_fit or 'cover'};'"/>
      </t>
      <t t-else="">
        <img src="/company_sale_report_cover/static/src/img/default_cover.jpg"
             style="width:100%; height:100%; object-fit: cover; display:block; margin:0;"/>
      </t>
    </div>

Optional: hide header/footer on the first page only (place in your report template or a separate asset bundle):
--------------------------------------------------------------------------------------------------------------
    <style type="text/css">
      .page:first-child .header, 
      .page:first-child .footer {
        display: none !important;
      }
      .page:first-child { padding: 0 !important; }
    </style>

How to install:
---------------
1) Zip the module folder and upload to your Odoo addons path (or place the unzipped folder).
2) Update Apps list and install "Company Sale Report Cover".
3) Go to Settings > Companies, open your company, tab "Report Cover", upload the image, choose fit.
4) Add the snippet above to your report template.

Tested on Odoo 18. Should also work on Odoo 16/17.