# -*- coding: utf-8 -*-

from odoo import fields, models,tools,api

class PosPaymentMethod(models.Model):
    _inherit = 'pos.payment.method'

    allow_card_charges = fields.Boolean('Allow card charges')
    allow_limit_amount = fields.Boolean('Allow Limit Amount')
    charges_type = fields.Selection([('percentage', 'Percentage'),('fixed', 'Fix')],string="Charges type", default='percentage')
    wv_amount = fields.Float("Amount")
    amount_min = fields.Float("Min Amount", default=0)
    amount_max = fields.Float("Max Amount", default=0)
    card_product = fields.Many2one("product.product",string="Card Charge Product",domain=[('available_in_pos','=',True),('type','=','service')])
