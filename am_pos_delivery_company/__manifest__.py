# -*- coding: utf-8 -*-

{
	"name" : "POS Delivery Company Buttons",
	"version" : "15.0.0.0",
	"category" : "Point of Sale",
	"depends" : ['base','point_of_sale'],
	"author": "Ahmed Elmahdi",
	'summary': '',
	"description": """

	""",

	"data": [
		'views/pos_assets.xml',
	],
	# 'qweb': [
	# 	'static/src/xml/ControlButtons.xml',
	# ],
	'assets': {
        'point_of_sale.assets': [
            'am_pos_delivery_company/static/src/js/ControlButtons.js',
        ],
        'web.assets_qweb': [
            'am_pos_delivery_company/static/src/xml/ControlButtons.xml',
        ],
    },
    'images':['static/description/image.png'],
	
	"auto_install": False,
	"installable": True,

}
