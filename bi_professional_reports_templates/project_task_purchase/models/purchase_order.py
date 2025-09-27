# -*- coding: utf-8 -*-
from odoo import api, fields, models

class PurchaseOrder(models.Model):
    _inherit = "purchase.order"

    task_id = fields.Many2one(
        "project.task",
        string="Task",
        index=True,
        ondelete="set null",
        help="The project task related to this Purchase Order.",
    )

    # Related project for compatibility with any views referencing project on POs
    project_id = fields.Many2one(
        "project.project",
        string="Project",
        related="task_id.project_id",
        store=True,
        readonly=True,
        index=True,
        help="Project of the related task (if any)."
    )

    @api.onchange('task_id')
    def _onchange_task_id_set_origin(self):
        for po in self:
            if po.task_id:
                po.origin = po.task_id.display_name
