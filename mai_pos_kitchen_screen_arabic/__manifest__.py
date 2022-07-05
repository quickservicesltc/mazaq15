{
    'name': 'POS Kitchen Receipt Arabic || POS Arabic Receipt with Kitchen order Receipt',
    'description': """
     Using This module you can print POS Kitchen Receipt Arabic with one is for a customer and one for a kitchen cook for order details.
    """,
    'version': '3.2.1',
    'sequence': 1,
    'email': 'apps@maisolutionsllc.com',
    'website':'http://maisolutionsllc.com/',
    'category': 'Point of Sale',
    'summary': 'Using This module you can print POS Kitchen Receipt Arabic with one is for a customer and one for a kitchen cook for order details.',
    'author': 'MAISOLUTIONSLLC',
    'price': 15,
    'currency': 'EUR',
    'license': 'OPL-1',
    'depends': ['point_of_sale', 'pos_restaurant','contacts_unique_code'],
    # "live_test_url" : "",
    # 'qweb': [
    #          'static/src/xml/templates.xml',
    #          ],
    'data': [
        # 'views/pos_receipt_template.xml',
             'views/product_view.xml',
             'views/config_view.xml',
             ],
    'assets': {
        'point_of_sale.assets': [
            'mai_pos_kitchen_screen_arabic/static/src/js/**/*.js',
        ],
        'web.assets_qweb': [
            'mai_pos_kitchen_screen_arabic/static/src/xml/templates.xml',
        ],
    },
    'images': ['static/description/main_screenshot.png'],
    "live_test_url" : "https://youtu.be/cOFhcIrrWMM ",
    'demo': [],
    'installable': True,
    'auto_install': False,
    'application': True,
}
