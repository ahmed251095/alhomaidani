# -*- coding: utf-8 -*-
from odoo import models, fields

class ResCompany(models.Model):
    _inherit = 'res.company'

    default_extra_print_html = fields.Html(
        string="Default Quotation Extra HTML",
        sanitize=True,
        strip_style=False,
        translate=True,
        help="النص الافتراضي الذى سيظهر تلقائياً فى تبويب HTML داخل أمر البيع الجديد."
    )
