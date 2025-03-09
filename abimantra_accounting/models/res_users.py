from odoo import models, fields, api, _

class ResUsers(models.Model):
    _inherit = 'res.users'

    branch_id = fields.Many2one('branch', string='Branch')