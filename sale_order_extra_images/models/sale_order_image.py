# -*- coding: utf-8 -*-
from odoo import api, fields, models

class SaleOrderImage(models.Model):
    _name = "sale.order.image"
    _description = "Sale Order Extra Image"
    _order = "sequence, id"

    sale_id = fields.Many2one("sale.order", string="Sale Order", required=True, ondelete="cascade")
    sequence = fields.Integer(default=10)
    name = fields.Char("Caption")
    image_1920 = fields.Image("Image", max_width=1920, max_height=1920, required=True)
    image_1024 = fields.Image(related="image_1920", max_width=1024, max_height=1024, store=True)
    active = fields.Boolean(default=True)

class SaleOrder(models.Model):
    _inherit = "sale.order"
    extra_image_ids = fields.One2many("sale.order.image", "sale_id", string="Print Images")
