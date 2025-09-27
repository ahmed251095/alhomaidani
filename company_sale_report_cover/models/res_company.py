# -*- coding: utf-8 -*-
from odoo import models, fields

class ResCompany(models.Model):
    _inherit = "res.company"

    sale_report_cover = fields.Binary(
        string="Sale Report Cover (JPEG/PNG)",
        attachment=True,
        help="This image will be used as the first-page cover for sale order reports if your template includes it."
    )
    sale_report_cover_fit = fields.Selection([
        ("contain", "Contain"),
        ("cover", "Cover"),
        ("fill", "Fill"),
        ("none", "None"),
        ("scale-down", "Scale down"),
    ], string="Cover Object-Fit", default="cover",
       help="How the image scales inside the page area when used in the report cover.")

    sale_report_cover_filename = fields.Char(string="Cover Filename")
