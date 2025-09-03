# -*- coding: utf-8 -*-
from odoo import api, fields, models

class PurchaseOrder(models.Model):
    _inherit = "purchase.order"

    task_id = fields.Many2one(
        "project.task",
        string="Task",
        index=True,
        help="The project task related to this Purchase Order.",
    )

    @api.onchange('task_id')
    def _onchange_task_id_set_origin(self):
        for po in self:
            if po.task_id:
                po.origin = po.task_id.display_name
