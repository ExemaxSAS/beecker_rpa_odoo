# -*- coding: utf-8 -*-
import logging

import odoo
from odoo import http
from odoo.http import request
import re
import xmlrpc.client

_logger = logging.getLogger(__name__)
CORS = '*'

class BeeckerOdooSaleOrderApi(http.Controller):

    @http.route('/beecker-api/sale_order/create', type="json", auth='none', cors='*')
    def beecker_create_sale_order(self, db=None, login=None, password=None, partner_id=None, order_line=[], company=1, **kw):
        try:
            uid = request.session.authenticate(db, login, password)
            if uid:
                if partner_id:
                    partner = request.env['res.partner'].sudo().search([('id', '=', partner_id)], limit=1)
                    saleorder = request.env['sale.order'].with_context(mail_create_nosubscribe=True, force_company=company).sudo().create({
                        'partner_id': partner_id,
                        'partner_invoice_id': partner_id,
                        'partner_shipping_id': partner_id,
                        'pricelist_id': partner.property_product_pricelist.id,
                    })

                if saleorder:
                    if order_line:
                        for line in order_line:
                            n_line = request.env['sale.order.line'].with_context(mail_create_nosubscribe=True, force_company=company).sudo().create({
                                'order_id': saleorder.id,
                                'product_id': line['id'],
                                'product_uom_qty': line['qty'],
                            })

                return {
                    'name': saleorder.name,
                    'id': saleorder.id,
                    'status': 'Ok'
                }
            else:
                return {'status': "Error"}
        except Exception as e:
            return {'status': "Error", 'error': str(e)}
