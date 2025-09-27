# -*- coding: utf-8 -*-
from odoo import api, fields, models, _

class ProjectTask(models.Model):
    _inherit = "project.task"

    purchase_order_ids = fields.One2many(
        "purchase.order", "task_id", string="Purchase Orders"
    )
    purchase_order_count = fields.Integer(
        string="PO Count", compute="_compute_purchase_order_count", store=False
    )

    @api.depends('purchase_order_ids')
    def _compute_purchase_order_count(self):
        # efficient count using read_group
        groups = self.env['purchase.order'].read_group(
            [('task_id', 'in', self.ids)], ['task_id'], ['task_id']
        )
        count_map = {g['task_id'][0]: g['task_id_count'] for g in groups}
        for task in self:
            task.purchase_order_count = count_map.get(task.id, 0)

    def action_create_purchase_order(self):
        self.ensure_one()
        action = self.env.ref("purchase.purchase_form_action").read()[0]
        action.update({
            "view_mode": "form",
            "views": [(False, "form")],
            "target": "current",
            "context": {
                "default_task_id": self.id,
                "default_origin": self.display_name or self.name,
            }
        })
        return action

    def action_open_purchase_orders(self):
        self.ensure_one()
        action = self.env.ref("purchase.purchase_rfq").read()[0]
        action.update({
            "domain": [("task_id", "=", self.id)],
            "context": {"default_task_id": self.id},
        })
        return action
