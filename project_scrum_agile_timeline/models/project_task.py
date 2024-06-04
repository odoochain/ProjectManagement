# Copyright 2024 Onestein (<http://www.onestein.eu>)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo import api, models


class ProjectTask(models.Model):
    _inherit = "project.task"

    @api.model_create_multi
    def create(self, vals_list):
        for vals in vals_list:
            if vals.get('sprint_id'):
                sprint_rec = self.env['project.scrum.sprint'].browse(vals.get('sprint_id'))
                vals["date_start"] = sprint_rec.date_start
                vals["date_end"] = sprint_rec.date_stop
        return super(ProjectTask, self).create(vals_list)

    def write(self, vals):
        if vals.get("sprint_id"):
            sprint_rec = self.env['project.scrum.sprint'].browse(vals.get('sprint_id'))
            vals["date_start"] = sprint_rec.date_start
            vals["date_end"] = sprint_rec.date_stop
        return super(ProjectTask, self).write(vals)
