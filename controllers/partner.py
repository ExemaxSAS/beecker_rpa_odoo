# -*- coding: utf-8 -*-
import logging

import odoo
from odoo import http
from odoo.http import request
import re
import xmlrpc.client

_logger = logging.getLogger(__name__)
CORS = '*'

class BeeckerOdooPartnerApi(http.Controller):

    @http.route('/beecker-api/partners/count', type="json", auth='none', cors=CORS)
    def partners_count(self, filters=None, **kw):
        try:
            uid = request.session.authenticate(db, login, password)
            if uid:
                partners = request.env['res.partner'].search(filters)
                return len(partners)
        except Exception as e:
            return {'status': False, 'error': str(e)}

    @http.route('/beecker-api/partners/get', type="json", auth='none', cors=CORS)
    def partners_get(self, filters=None, offset=0, **kw):
        try:
            uid = request.session.authenticate(db, login, password)
            if uid:
                partners = request.env['res.partner'].search_read(filters, limit=20, offset=offset, fields=['name', 'id'])
                return partners
        except Exception as e:
            return {'status': False, 'error': str(e)}
