# -*- coding: utf-8 -*-
from odoo import api, fields, models


class pos_config(models.Model):
    _inherit = 'pos.config' 

    restrict_offline = fields.Boolean('Restrict Offline')

    @api.model
    def check_online_mode(self):
        return {'mode': True}
