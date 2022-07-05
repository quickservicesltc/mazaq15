odoo.define('pw_pos_restrict_offline.PaymentScreen', function (require) {
"use strict";

    const PaymentScreen = require('point_of_sale.PaymentScreen');
    const Registries = require('point_of_sale.Registries');
    var core = require('web.core');
    var _t = core._t;

    const PosOfflineMode = PaymentScreen => class extends PaymentScreen {
        async validateOrder(isForceValidate) {
            if(this.env.pos.config.restrict_offline){
                try {
                    const result = await this.rpc({
                        model: 'pos.config',
                        method: 'check_online_mode',
                        args: [],
                    });
                    if(result && result.mode){
                        super.validateOrder(isForceValidate);
                    };
                } catch (error) {
                    if (error.message.code < 0) {
                        await this.showPopup('ErrorPopup', {
                            title: this.env._t('Offline'),
                            body: this.env._t('Please check your Internet connection.'),
                        });
                    } else {
                        throw error;
                    }
                }
            }
            else{
                super.validateOrder(isForceValidate);
            }
        }
    };

    Registries.Component.extend(PaymentScreen, PosOfflineMode);

    return PaymentScreen;
});

