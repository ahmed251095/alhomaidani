
# -*- coding: utf-8 -*-
from odoo import models, fields

class SaleOrder(models.Model):
    _inherit = "sale.order"

    service_type_id = fields.Many2one(
        "sale.product.service.type",
        string="نوع المنتجات والخدمات",
        tracking=True,
    )
