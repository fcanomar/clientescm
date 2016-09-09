# -*- coding: utf-8 -*-
from openerp import http

# class Clientescm(http.Controller):
#     @http.route('/clientescm/clientescm/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/clientescm/clientescm/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('clientescm.listing', {
#             'root': '/clientescm/clientescm',
#             'objects': http.request.env['clientescm.clientescm'].search([]),
#         })

#     @http.route('/clientescm/clientescm/objects/<model("clientescm.clientescm"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('clientescm.object', {
#             'object': obj
#         })