from odoo import fields, models

class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    extra_print_html_default = fields.Html(
        string='Default Extra Print HTML',
        config_parameter='sale.extra_print_html_default'
    )
