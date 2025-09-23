# -*- coding: utf-8 -*-
from odoo import models, fields, _

class SaleApprovalRejectWizard(models.TransientModel):
    _name = "sale.approval.reject.wizard"
    _description = "Reject Quotation Wizard"

    sale_id = fields.Many2one("sale.order", required=True)
    reason = fields.Text(required=True, string="Rejection Reason")

    def action_reject(self):
        self.ensure_one()
        sale = self.sale_id
        sale.write({
            "approval_state":"rejected",
            "rejection_reason": self.reason,
        })
        sale.message_post(body=_("Quotation rejected by %s.<br/>Reason: %s") % (self.env.user.display_name, self.reason))
        return {"type":"ir.actions.act_window_close"}