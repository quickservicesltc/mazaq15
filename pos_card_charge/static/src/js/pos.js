odoo.define('pos_card_charge.pos_card_charge', function (require) {
"use strict";

    const models = require('point_of_sale.models');
    const PaymentScreen = require('point_of_sale.PaymentScreen');
    const PosComponent = require('point_of_sale.PosComponent');
    const { useListener } = require('web.custom_hooks');
    const Registries = require('point_of_sale.Registries');
    const ProductScreen = require('point_of_sale.ProductScreen');
    const AbstractAwaitablePopup = require('point_of_sale.AbstractAwaitablePopup');

    models.load_fields("pos.payment.method",['allow_card_charges','charges_type','wv_amount','card_product','allow_limit_amount','amount_min','amount_max']);

    var PaymentlineSuper = models.Paymentline;
    models.Paymentline = models.Paymentline.extend({
        get_card_charges(){
            var line = this;
            if(line.payment_method.allow_card_charges){
                var payment_method = line.payment_method;
                if (payment_method.allow_limit_amount) {
                  if (payment_method.amount_min <= line.amount && (!payment_method.amount_max || payment_method.amount_max >= line.amount  )) {
                    if(payment_method.charges_type == "percentage"){
                        return (payment_method.wv_amount * line.get_amount())/100
                    }
                    else{
                        return payment_method.wv_amount;
                    }
                  }else {
                    return 0;
                  }

                }else {
                  if(payment_method.charges_type == "percentage"){
                      return (payment_method.wv_amount * line.get_amount())/100
                  }
                  else{
                      return payment_method.wv_amount;
                  }
                }

            }
            return 0;
        }
    });
    const PaymentScreen2 = (PaymentScreen) => {
        class PaymentScreen2 extends PaymentScreen {
            async validateOrder(isForceValidate) {
                if (await this._isOrderValid(isForceValidate)) {
                    var order = this.env.pos.get_order();
                    var plines = this.paymentLines;
                    for (var i = 0; i < plines.length; i++) {
                        if(plines[i].payment_method.allow_card_charges){
                            var card_Charge = plines[i].get_card_charges();

                            plines[i].amount += card_Charge;
                            var product_id = plines[i].payment_method.card_product[0];
                            var product = this.env.pos.db.get_product_by_id(product_id);
                            if (card_Charge) {
                              order.add_product(product,{ price: card_Charge })
                            }
                        }
                    }
                    for (let line of this.paymentLines) {
                        if (!line.is_done()) this.currentOrder.remove_paymentline(line);
                    }
                    await this._finalizeValidation();
                }
            }

        }
        return PaymentScreen2;
    };
    Registries.Component.extend(PaymentScreen, PaymentScreen2);
});
