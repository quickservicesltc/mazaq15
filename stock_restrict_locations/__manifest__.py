# -*- coding: utf-8 -*-
#
# Copyright © Ryan Cole 2017-Present
#   - https://www.ryanc.me/
#   - admin@ryanc.me
#
# Please see the LICENSE file for license details


{
    "name": "Stock Location Restrictions",
    "summary": "Restrict stock locations, warehouses, "
               "and picking types per user",
    "description": "Restrict stock locations, warehouses, "
                   "and picking types per user",

    "currency": "EUR",
    "price": 24.99,

    "version": "14.0.1.0",
    "license": "Other proprietary",
    "author": "Ryan Cole <hello@ryanc.me>",
    "maintainer": "Ryan Cole <hello@ryanc.me>",
    "website": "https://www.ryanc.me/contact/#stock_user_restrictions",

    "category": "Warehouse",
    "complexity": "Normal",
    "application": False,
    "installable": True,

    "images": [
        "static/description/banner.png"
    ],

    "depends": [
        "stock",
    ],

    "data": [
        "views/views.xml",
        "security/access_rules.xml",
    ],

    "post_init_hook": "post_init_hook",
}
