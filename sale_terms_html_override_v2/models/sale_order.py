# -*- coding: utf-8 -*-
from odoo import fields, models

class SaleOrder(models.Model):
    _inherit = "sale.order"
    # Keep same technical name, change to HTML (in case another module reverted it)
    note = fields.Html(string="Terms & Conditions", sanitize=False)
