# -*- coding: utf-8 -*-
# from odoo import http


# class AbimantraAccounting(http.Controller):
#     @http.route('/abimantra_accounting/abimantra_accounting', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/abimantra_accounting/abimantra_accounting/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('abimantra_accounting.listing', {
#             'root': '/abimantra_accounting/abimantra_accounting',
#             'objects': http.request.env['abimantra_accounting.abimantra_accounting'].search([]),
#         })

#     @http.route('/abimantra_accounting/abimantra_accounting/objects/<model("abimantra_accounting.abimantra_accounting"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('abimantra_accounting.object', {
#             'object': obj
#         })
