from odoo import api, models

class SaleOrder(models.Model):
    _inherit = "sale.order"

    @api.model_create_multi
    def create(self, vals_list):
        # Fetch default from config parameter
        ICP = self.env['ir.config_parameter'].sudo()
        default_html = ICP.get_param('sale.default_extra_print_html', default='') or ''
        # Only set if field exists and value not provided
        has_field = 'extra_print_html' in self._fields
        for vals in vals_list:
            if has_field and not vals.get('extra_print_html') and default_html:
                vals['extra_print_html'] = default_html
        return super().create(vals_list)