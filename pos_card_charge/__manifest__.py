# -*- coding: utf-8 -*-

{
    'name': 'Pos Card charges',
    'version': '1.0',
    'category': 'Point of Sale',
    'sequence': 6,
    'author': 'Webveer',
    'summary': 'Pos Card charges.',
    'description': """

=======================

Pos Card charges.

""",
    'depends': ['point_of_sale'],
    'data': [
        'views/views.xml',
        # 'views/templates.xml'
    ],
    # 'qweb': [
    #     'static/src/xml/pos.xml',
    # ],
    'assets': {
        'point_of_sale.assets': [
            'pos_card_charge/static/src/js/pos.js',
        ],
        'web.assets_qweb': [
            'pos_card_charge/static/src/xml/pos.xml',
        ],
    },
    'images': [
        'static/description/config.jpg',
    ],
    'installable': True,
    'website': '',
    'auto_install': False,
    'price': 18,
    'currency': 'EUR',
}
