# -*- coding: utf-8 -*-

from odoo import fields, models, api, _, tools
from datetime import date, time, datetime
import psycopg2
import logging
_logger = logging.getLogger(__name__)

class PosConfig(models.Model):
	_inherit = 'pos.config'

	hide_kitchen_receipt = fields.Boolean(string='Hide Kitchen Receipt')
