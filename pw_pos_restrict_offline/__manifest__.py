# -*- coding: utf-8 -*-
{
    'name': 'POS Restrict Offline Mode',
    'version': '15.0',
    'author': 'Preway IT Solutions',
    'category': 'Point of Sale',
    'depends': ['point_of_sale'],
    'summary': 'This apps allows you to restrict pos session work in offline mode | POS Online Mode | POS Disable Offline',
    'description': """
- Odoo POS Online Mode
    """,
    'data': [
        # 'views/assets.xml',
        'views/pos_config_view.xml',
    ],
    'assets': {
        'point_of_sale.assets': [
            'pw_pos_restrict_offline/static/src/js/PaymentScreen.js',
        ],
    },
    'price': 20.0,
    'currency': "EUR",
    'application': True,
    'installable': True,
    "images":["static/description/Banner.png"],
}
