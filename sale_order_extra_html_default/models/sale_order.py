# -*- coding: utf-8 -*-
from odoo import models, fields

class SaleOrder(models.Model):
    _inherit = 'sale.order'

    extra_print_html = fields.Html(
        string="Additional Text",
        sanitize=True,
        strip_style=False,
        translate=True,
        default=lambda self: self.env.company.default_extra_print_html or False,
    )

    def action_set_extra_as_company_default(self):
        for order in self:
            order.company_id.default_extra_print_html = order.extra_print_html or False
