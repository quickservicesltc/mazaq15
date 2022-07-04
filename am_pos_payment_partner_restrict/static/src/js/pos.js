odoo.define('am_pos_payment_partner_restrict.pos', function (require) {
"use strict";

    const models = require('point_of_sale.models');
    const PaymentScreen = require('point_of_sale.PaymentScreen');
    const { useListener } = require('web.custom_hooks');
    const Registries = require('point_of_sale.Registries');
    const ProductScreen = require('point_of_sale.ProductScreen');
    const AbstractAwaitablePopup = require('point_of_sale.AbstractAwaitablePopup');

    models.load_fields('res.partner', ['payment_methods']);


    const PaymentScreen2 = (PaymentScreen) => {
        class PaymentScreen2 extends PaymentScreen {
            constructor() {
                super(...arguments);
                var currentOrder = this.env.pos.get_order();
                var client = currentOrder.get_client();
                if (client && client.payment_methods.length>0) {
                  this.payment_methods_from_config = this.payment_methods_from_config.filter(method => client.payment_methods.includes(method.id));
                }
            }
        }
        return PaymentScreen2;
    };
    Registries.Component.extend(PaymentScreen, PaymentScreen2);

});
