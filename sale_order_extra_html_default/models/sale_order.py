from odoo import api, models

class SaleOrder(models.Model):
    _inherit = 'sale.order'

    @api.model_create_multi
    def create(self, vals_list):
        # Get default from system parameter
        default_html = self.env['ir.config_parameter'].sudo().get_param(
            'sale.extra_print_html_default', default=''
        )
        for vals in vals_list:
            # If the custom HTML field exists in the DB (provided by sale_order_extra_images)
            # and is empty, prefill it with the default value.
            if 'extra_print_html' in self._fields and not vals.get('extra_print_html'):
                vals['extra_print_html'] = default_html
        return super().create(vals_list)
