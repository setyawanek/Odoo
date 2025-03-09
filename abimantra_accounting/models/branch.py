from odoo import models, fields

class Branch(models.Model):
    _name = 'branch'
    _description = 'Branch'

    name = fields.Char(string='Code Name')
    branch = fields.Char(string='Branch name')