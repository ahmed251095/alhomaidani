# -*- coding: utf-8 -*-
from odoo import models, fields, api, _
from odoo.exceptions import ValidationError

class SaleOrder(models.Model):
    _inherit = "sale.order"

    approval_state = fields.Selection([
        ("draft","Draft"),
        ("waiting","Waiting L1 Approval"),
        ("level1","Waiting L2 Approval"),
        ("approved","Approved"),
        ("rejected","Rejected"),
    ], default="draft", copy=False, string="Approval State", tracking=True)
    approver1_id = fields.Many2one("res.users", string="Level 1 Approved By", copy=False, readonly=True)
    approver1_date = fields.Datetime(string="Level 1 Approval Date", copy=False, readonly=True)
    approver2_id = fields.Many2one("res.users", string="Level 2 Approved By", copy=False, readonly=True)
    approver2_date = fields.Datetime(string="Level 2 Approval Date", copy=False, readonly=True)
    approval_note = fields.Text(string="Approval Note")
    rejection_reason = fields.Text(string="Rejection Reason", readonly=True, copy=False)

    def _notify_group(self, xmlid):
        group = self.env.ref(xmlid, raise_if_not_found=False)
        if not group:
            return
        activity_type = self.env.ref("mail.mail_activity_data_todo", raise_if_not_found=False)
        for order in self:
            partner_ids = []
            for user in group.users:
                partner_ids.append(user.partner_id.id)
                if activity_type:
                    self.env["mail.activity"].sudo().create({
                        "activity_type_id": activity_type.id,
                        "res_model_id": self.env["ir.model"]._get_id("sale.order"),
                        "res_id": order.id,
                        "user_id": user.id,
                        "summary": _("Approve quotation"),
                        "note": _("Please review and approve quotation %s.") % (order.name or _("(New)")),
                    })
            if partner_ids:
                order.message_post(
                    body=_("Approval requested for quotation."),
                    partner_ids=partner_ids,
                    subtype_xmlid="mail.mt_comment",
                )

    def action_submit_for_approval(self):
        for order in self:
            if order.state not in ("draft","sent"):
                raise ValidationError(_("Only draft/sent quotations can be submitted."))
            order.write({"approval_state":"waiting", "rejection_reason": False})
        self._notify_group("sale_approval_flow_v2.group_sale_approve_level1")
        return True

    def action_approve_level1(self):
        self.ensure_one()
        if self.approval_state != "waiting":
            raise ValidationError(_("Quotation must be in 'Waiting L1 Approval'."))
        self.write({
            "approval_state":"level1",
            "approver1_id": self.env.user.id,
            "approver1_date": fields.Datetime.now(),
            "rejection_reason": False,
        })
        self.message_post(body=_("Approved by Level 1: %s.") % self.env.user.display_name)
        self._notify_group("sale_approval_flow_v2.group_sale_approve_level2")
        return True

    def action_approve_level2(self):
        self.ensure_one()
        if self.approval_state != "level1":
            raise ValidationError(_("Quotation must be in 'Waiting L2 Approval'."))
        self.write({
            "approval_state":"approved",
            "approver2_id": self.env.user.id,
            "approver2_date": fields.Datetime.now(),
        })
        self.message_post(body=_("Approved by Level 2: %s.") % self.env.user.display_name)
        return True

    def action_reject_open_wizard(self):
        self.ensure_one()
        if self.approval_state not in ("waiting","level1"):
            raise ValidationError(_("Only quotations pending approval can be rejected."))
        return {
            "type":"ir.actions.act_window",
            "res_model":"sale.approval.reject.wizard",
            "view_mode":"form",
            "target":"new",
            "context":{"default_sale_id": self.id},
        }

    def action_confirm(self):
        for order in self:
            if order.approval_state != "approved":
                raise ValidationError(_("You cannot confirm this quotation until Level 2 approval is completed."))
        return super().action_confirm()