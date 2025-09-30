
# -*- coding: utf-8 -*-
from odoo import models, fields

class SaleProductServiceType(models.Model):
    _name = "sale.product.service.type"
    _description = "Product/Service Type for Sales"
    _order = "sequence, name"

    name = fields.Char(required=True, translate=True)
    sequence = fields.Integer(default=10)
    company_id = fields.Many2one(
        "res.company",
        string="Company",
        default=lambda self: self.env.company,
        help="Leave empty to make it available to all companies."
    )
    active = fields.Boolean(default=True)
    note = fields.Html()
