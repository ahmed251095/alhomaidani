# -*- coding: utf-8 -*-
from odoo import fields, models

class SaleOrder(models.Model):
    _inherit = "sale.order"

    extra_print_html = fields.Html(
        string="Extra Print HTML",
        sanitize=False,
        help="Rich text (HTML) that will be printed after Terms & Conditions."
    )
