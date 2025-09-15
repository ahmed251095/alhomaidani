from odoo import models, fields, api

class SaleOrder(models.Model):
    _inherit = 'sale.order'

    report_field = fields.Html(string='Report Field')

