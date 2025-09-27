
# -*- coding: utf-8 -*-
from odoo import api, models

class SaleOrder(models.Model):
    _inherit = 'sale.order'

    @api.model_create_multi
    def create(self, vals_list):
        # Fill extra_print_html from config once at creation if the field exists and value is empty.
        ICP = self.env['ir.config_parameter'].sudo()
        default_html = ICP.get_param('sale_order_extra_html_default_safe.default_html', default='')
        new_list = []
        for vals in vals_list:
            # only if the target field exists on this DB and is not already provided
            if hasattr(self, 'extra_print_html') and not vals.get('extra_print_html') and default_html:
                v = dict(vals)
                v['extra_print_html'] = default_html
                new_list.append(v)
            else:
                new_list.append(vals)
        return super().create(new_list)
