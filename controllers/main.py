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
