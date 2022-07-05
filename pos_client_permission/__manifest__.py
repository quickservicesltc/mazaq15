# -*- coding: utf-8 -*-

{
    "name" : "POS Hide Client Button",
    "version" : "15.0",
    'category' : 'Sales/Point of Sale',
    "depends" : ['base','point_of_sale'],
    "author": "Ahmed Elmahdi",
    'summary': '''
    POS Hide Client Button
    POS Client Required before validate order
    ''',
    "price": 5,
    "currency": "EUR",
    "license": "LGPL-3",
    "description": """
POS Hide Client Button
Create Button
Edit Button
Required Client
    """,
    "data": [
        'views/custom_config_view.xml',
    ],
    # 'qweb': [
    #     'static/src/xml/pos_extended.xml',
    # ],
    'assets': {
        'point_of_sale.assets': [
            'pos_client_permission/static/src/js/pos.js',
        ],
        'web.assets_qweb': [
            'pos_client_permission/static/src/xml/pos_extended.xml',
        ],
    },
    "auto_install": False,
    "installable": True,
    "images":['static/description/showHideButton.png'],
}
