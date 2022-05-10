# -*- coding: utf-8 -*-

# from odoo import models, fields, api


# class beecker_rpa_odoo(models.Model):
#     _name = 'beecker_rpa_odoo.beecker_rpa_odoo'
#     _description = 'beecker_rpa_odoo.beecker_rpa_odoo'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
