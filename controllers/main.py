# -*- coding: utf-8 -*-
import logging

import odoo
from odoo import http
from odoo.http import request
import re
import xmlrpc.client

_logger = logging.getLogger(__name__)
CORS = '*'

class BeeckerOdooApi(http.Controller):

    @http.route('/beecker-api/common/version', type="json", auth='none', cors=CORS)
    def odoo_api_version(self, **kw):
        common = xmlrpc.client.ServerProxy('http://127.0.0.1:8069/xmlrpc/2/common')
        return common.version()

    @http.route('/beecker-api/company/get', type="json", auth='none', cors=CORS)
    def company_get(self, db=None, login=None, password=None, **kw):
        try:
            uid = request.session.authenticate(db, login, password)
            if uid:
                company = request.env['res.company'].search_read([], fields=['name', 'id'])
                return company
        except Exception as e:
            return {'status': "Error", 'error': str(e)}
