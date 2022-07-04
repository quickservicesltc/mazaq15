# -*- coding: utf-8 -*-

{
    'name': 'POS Payment Method Partner Restrict',
    'version': '15.0',
    'category': 'Point of Sale',
    'sequence': 6,
    'author': 'Ahmed Elmahdi',
    'summary': 'POS Payment Method Partner Restrict',
    'description': """
    POS Payment Method Restrict
    POS Payment Partner Restrict
    POS Payment Method Partner Restrict
    Restrict Payment Method depends on Payment Selected In Partner
    Select Payment Method For each Partner
    Select Payment Method For each Contact
""",
    'category': 'Point of Sale',
    'depends': ['point_of_sale'],
    'data': [
        'views/views.xml',
    ],
    'license': 'LGPL-3',
    'assets': {
        'point_of_sale.assets': [
            'am_pos_payment_partner_restrict/static/src/js/pos.js',
        ],
        # 'web.assets_qweb': [
        #     'am_pos_payment_partner_restrict/static/src/xml/pos.xml',
        # ],
    },
    'images':['static/description/image.png'],

    'installable': True,
    'auto_install': False,
    'price': 7,
    'currency': 'EUR',
}
