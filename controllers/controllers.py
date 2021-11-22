# -*- coding: utf-8 -*-
from odoo import http

# class MethodRefGuia(http.Controller):
#     @http.route('/method_ref_guia/method_ref_guia/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/method_ref_guia/method_ref_guia/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('method_ref_guia.listing', {
#             'root': '/method_ref_guia/method_ref_guia',
#             'objects': http.request.env['method_ref_guia.method_ref_guia'].search([]),
#         })

#     @http.route('/method_ref_guia/method_ref_guia/objects/<model("method_ref_guia.method_ref_guia"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('method_ref_guia.object', {
#             'object': obj
#         })