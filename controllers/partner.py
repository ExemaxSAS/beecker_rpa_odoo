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
    def partners_count(self, db=None, login=None, password=None, filters=[], **kw):
        try:
            uid = request.session.authenticate(db, login, password)
            if uid:
                partners = request.env['res.partner'].search(filters)
                return len(partners)
        except Exception as e:
            return {'status': "Error", 'error': str(e)}

    @http.route('/beecker-api/partners/get', type="json", auth='none', cors=CORS)
    def partners_get(self, db=None, login=None, password=None, filters=[], name=None, email=None, offset=0, **kw):
        try:
            uid = request.session.authenticate(db, login, password)
            if uid:
                if name:
                    partners = request.env['res.partner'].search_read([('name', 'like', name)], limit=20, offset=offset, fields=['name', 'id'])
                elif email:
                    partners = request.env['res.partner'].search_read([('email', '=', email)], limit=20, offset=offset, fields=['name', 'id'])
                else:
                    partners = request.env['res.partner'].search_read(filters, limit=20, offset=offset, fields=['name', 'id'])
                return partners
        except Exception as e:
            return {'status': "Error", 'error': str(e)}

    @http.route('/beecker-api/partners/search', type="json", auth='none', cors=CORS)
    def partners_search(self, db=None, login=None, password=None, name=None, email=None, offset=0, **kw):
        try:
            uid = request.session.authenticate(db, login, password)
            if uid:
                if name:
                    partners = request.env['res.partner'].search_read([('name', 'like', name)], offset=offset, fields=['id'])
                    return partners
                if email:
                    partners = request.env['res.partner'].search_read([('email', '=', email)], offset=offset, fields=['id'])
                    return partners
        except Exception as e:
            return {'status': "Error", 'error': str(e)}

    @http.route('/beecker-api/partners/create', type="json", auth='none', cors=CORS)
    def partners_create(self, db=None, login=None, password=None, name='Demo', email=False, street=False, street2=False, country=False, state=False, city=False, zip=False, function=False, phone=False, mobile=False, website=False, **kw):
        try:
            uid = request.session.authenticate(db, login, password)
            if uid:
                country_id = False
                state_id = False
                if country:
                    country_id = request.env['res.country'].search_read([('name', 'like', country)], limit=1, fields=['id'])
                    if country_id:
                        country_id = country_id[0]['id']
                    else:
                        country_id = False
                if state:
                    state_id = request.env['res.country.state'].search_read([('name', 'like', state)], limit=1, fields=['id'])
                    if state_id:
                        state_id = state_id[0]['id']
                    else:
                        state_id = False
                _logger.info(country_id)
                partner = request.env['res.partner'].sudo().create({'name': name, 'email': email, 'street': street, 'street2': street2, 'country_id': country_id, 'state_id': state_id, 'city': city, 'zip': zip, 'function': function, 'phone': phone, 'mobile': mobile, 'website': website})
                return {
                    'name': partner.name,
                    'id': partner.id,
                    'status': 'Ok'
                }
        except Exception as e:
            return {'status': "Error", 'error': str(e)}
