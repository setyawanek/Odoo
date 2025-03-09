# -*- coding: utf-8 -*-

# from odoo import models, fields, api


# class abimantra_accounting(models.Model):
#     _name = 'abimantra_accounting.abimantra_accounting'
#     _description = 'abimantra_accounting.abimantra_accounting'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
