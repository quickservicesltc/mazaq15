# -*- coding: utf-8 -*-

from odoo import fields, models, api, _ , tools
from odoo.exceptions import Warning
import random
from datetime import date, datetime
from odoo.tools import DEFAULT_SERVER_DATETIME_FORMAT, DEFAULT_SERVER_DATE_FORMAT


class POSConfig(models.Model):
	_inherit = 'pos.config'

	TheChefz = fields.Boolean('The Chefz')
	Mrsool = fields.Boolean('Mrsool')
	Trker = fields.Boolean('TRKER')
	Toyo = fields.Boolean('TOYO')
	HungerStation = fields.Boolean('Hunger Station')
	Jahez = fields.Boolean('Jahez')
