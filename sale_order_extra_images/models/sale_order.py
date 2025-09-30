# -*- coding: utf-8 -*-
from odoo import fields, models

class SaleOrder(models.Model):
    _inherit = "sale.order"

    extra_print_html = fields.Html(
        string="Extra Print HTML",
        sanitize=False,
        help="Rich text (HTML) that will be printed after Terms & Conditions."
    )



@api.onchange('service_type_id')
    def _onchange_service_type_id_set_extra_html(self):
        """انسخ الملاحظة من نوع الخدمة عند تغييره في الفورم."""
        for order in self:
            order.extra_print_html = order.service_type_id.note or False

    @api.model
    def create(self, vals):
        """لو اتعمل إنشاء عبر RPC/Import ومش مبعوت extra_print_html
        انسخه من note."""
        if not vals.get('extra_print_html') and vals.get('service_type_id'):
            st = self.env['sale.product.service.type'].browse(vals['service_type_id'])
            vals['extra_print_html'] = st.note or False
        return super(SaleOrder, self).create(vals)

    def write(self, vals):
        """لو اتغير service_type_id بعد الإنشاء ومفيش extra_print_html متبعت،
        انسخه تلقائيًا."""
        if 'service_type_id' in vals and 'extra_print_html' not in vals:
            st = self.env['sale.product.service.type'].browse(vals['service_type_id'])
            vals['extra_print_html'] = st.note or False
        return super(SaleOrder, self).write(vals)
