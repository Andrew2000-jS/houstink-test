# -*- coding: utf-8 -*-
# from odoo import http


# class Houstink-test(http.Controller):
#     @http.route('/houstink-test/houstink-test', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/houstink-test/houstink-test/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('houstink-test.listing', {
#             'root': '/houstink-test/houstink-test',
#             'objects': http.request.env['houstink-test.houstink-test'].search([]),
#         })

#     @http.route('/houstink-test/houstink-test/objects/<model("houstink-test.houstink-test"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('houstink-test.object', {
#             'object': obj
#         })

