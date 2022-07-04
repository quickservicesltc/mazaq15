# -*- coding: utf-8 -*-

from odoo import fields, models,tools,api

class ResPartner(models.Model):
    _inherit = 'res.partner'

    payment_methods = fields.Many2many('pos.payment.method', string='Payment Methods')
