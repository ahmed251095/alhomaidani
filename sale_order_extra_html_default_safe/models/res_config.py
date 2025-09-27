from odoo import fields, models

class ResConfigSettings(models.TransientModel):
    _inherit = "res.config.settings"

    default_extra_print_html = fields.Html(
        string="Default Extra Print HTML",
        config_parameter="sale.default_extra_print_html",
        sanitize=False,
    )