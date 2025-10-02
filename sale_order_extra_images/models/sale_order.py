# from odoo import api,fields, models

# class SaleOrder(models.Model):
#     _inherit = "sale.order"

#     extra_print_html = fields.Html(
#         string="Extra Print HTML",
#         sanitize=False,
#         help="Rich text (HTML) that will be printed after Terms & Conditions."
#     )



# -*- coding: utf-8 -*-
from odoo import api, fields, models

class SaleOrder(models.Model):
    _inherit = "sale.order"

    extra_print_html = fields.Html(
        string="Extra Print HTML",
        sanitize=False,
        help="Rich text (HTML) that will be printed after Terms & Conditions."
    )

    note = fields.Html(
        string="Terms & Conditions",
        sanitize=False,
    )

    @api.onchange('service_type_id')
    def _onchange_service_type_id_set_extra_html(self):
        """انسخ الملاحظة من نوع الخدمة عند تغييره في الفورم.
        لو المستخدم كتب يدويًا قبل كده، ما نكتبش فوقه."""
        for order in self:
            if not order.extra_print_html:
                order.extra_print_html = order.service_type_id.note or False

    @api.model
    def create(self, vals):
        """لو اتعمل إنشاء عبر RPC/Import ومفيش extra_print_html،
        انسخه من note بتاع service_type_id."""
        if not vals.get('extra_print_html') and vals.get('service_type_id'):
            st = self.env['sale.product.service.type'].browse(vals['service_type_id'])
            vals['extra_print_html'] = st.note or False
        return super(SaleOrder, self).create(vals)

    def write(self, vals):
        """لو اتغير service_type_id ومفيش extra_print_html مبعوت في نفس الطلب،
        انسخه تلقائيًا من note. لو اتشال الـ service_type_id نخلي الحقل فاضي."""
        if 'service_type_id' in vals and 'extra_print_html' not in vals:
            st_id = vals.get('service_type_id')
            # في write غالبًا بيبقى int أو False
            if st_id:
                st = self.env['sale.product.service.type'].browse(st_id)
                vals['extra_print_html'] = st.note or False
            else:
                vals['extra_print_html'] = False
        return super(SaleOrder, self).write(vals)
