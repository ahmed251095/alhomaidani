
# -*- coding: utf-8 -*-
from odoo import api, fields, models, SUPERUSER_ID

class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    sale_extra_default_html = fields.Html(string='Default Extra Print HTML', config_parameter='sale_extra_html.default', sanitize=False)

    @api.model_create_multi
    def create(self, vals_list):
        # Call super, nothing fancy; values are stored via config_parameter
        return super().create(vals_list)

class SaleOrder(models.Model):
    _inherit = 'sale.order'

    extra_print_html = fields.Html()

    @api.model
    def create(self, vals):
        # Only set default if empty
        if not vals.get('extra_print_html'):
            param = self.env['ir.config_parameter'].sudo().get_param('sale_extra_html.default', False)
            if param:
                vals['extra_print_html'] = param
        return super().create(vals)
