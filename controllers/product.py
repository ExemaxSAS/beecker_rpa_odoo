# -*- coding: utf-8 -*-
import logging

import odoo
from odoo import http
from odoo.http import request
import re
import xmlrpc.client

_logger = logging.getLogger(__name__)
CORS = '*'

class BeeckerOdooProductApi(http.Controller):

    @http.route('/beecker-api/products/count', type="json", auth='none', cors=CORS)
    def products_count(self, filters=None, **kw):
        try:
            uid = request.session.authenticate(db, login, password)
            if uid:
                products = request.env['product.product'].search(filters)
                return len(products)
        except Exception as e:
            return {'status': False, 'error': str(e)}

    @http.route('/beecker-api/products/get', type="json", auth='none', cors=CORS)
    def partners_get(self, filters=None, offset=0, **kw):
        try:
            uid = request.session.authenticate(db, login, password)
            if uid:
                products = request.env['product.product'].search_read(filters, limit=20, offset=offset, fields=['name', 'id'])
                return products
        except Exception as e:
            return {'status': False, 'error': str(e)}

