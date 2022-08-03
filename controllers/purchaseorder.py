# -*- coding: utf-8 -*-
import logging

import odoo
from odoo import http
from odoo.http import request
import re
import xmlrpc.client

_logger = logging.getLogger(__name__)
CORS = '*'

class BeeckerOdooPurchaseOrderApi(http.Controller):

    @http.route('/beecker-api/purchase_order/create', type="json", auth='none', cors='*')
    def beecker_create_purchase_order(self, db=None, login=None, password=None, partner_id=None, order_line=[], company=1, **kw):
        try:
            uid = request.session.authenticate(db, login, password)
            if uid:
                if partner_id:
                    partner = request.env['res.partner'].sudo().search([('id', '=', partner_id)], limit=1)
                    purchaseorder = request.env['purchase.order'].with_context(mail_create_nosubscribe=True, force_company=company).sudo().create({
                        'partner_id': partner_id
                    })

                if purchaseorder:
                    if order_line:
                        for line in order_line:
                            n_line = request.env['purchase.order.line'].with_context(mail_create_nosubscribe=True, force_company=company).sudo().create({
                                'order_id': purchaseorder.id,
                                'product_id': line['id'],
                                'product_uom_qty': line['qty'],
                            })

                return {
                    'name': purchaseorder.name,
                    'id': purchaseorder.id,
                    'status': 'Ok'
                }
            else:
                return {'status': "Error"}
        except Exception as e:
            return {'status': "Error", 'error': str(e)}

    @http.route('/beecker-api/purchase_order/confirm', type="json", auth='none', cors='*')
    def beecker_confirm_purchase_order(self, db=None, login=None, password=None, purchase_order_id=None, **kw):
        try:
            uid = request.session.authenticate(db, login, password)
            if uid:
                purchase_order = request.env['purchase.order'].sudo().search([('id', '=', purchase_order_id)], limit=1)
                purchase_order_confirm = purchase_order.button_confirm()
                return {
                    'name': purchase_order.name,
                    'id': purchase_order.id,
                    'confirm': purchase_order_confirm,
                    'status': 'Ok'
                }
        except Exception as e:
            return {'status': "Error", 'error': str(e)}

    @http.route('/beecker-api/purchase_order/get', type="json", auth='none', cors='*')
    def beecker_get_purchase_order(self, db=None, login=None, password=None, purchase_order=None, **kw):
        try:
            uid = request.session.authenticate(db, login, password)
            if uid:
                purchase_order = request.env['purchase.order'].sudo().search([('name', '=', purchase_order)], limit=1)
                return {
                    'name': purchase_order.name,
                    'id': purchase_order.id,
                    'status': 'Ok'
                }
        except Exception as e:
            return {'status': "Error", 'error': str(e)}
