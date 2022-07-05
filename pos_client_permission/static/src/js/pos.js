odoo.define('pos_client_permission.pos', function(require){
	const PaymentScreen = require('point_of_sale.PaymentScreen');
	const PosComponent = require('point_of_sale.PosComponent');
	const Registries = require('point_of_sale.Registries');
	const { Component } = owl;


	const PaymentScreenWidget = (PaymentScreen) =>
		class extends PaymentScreen {


			async validateOrder(isForceValidate) {
				let self = this;
				let currentOrder = this.env.pos.get_order();
				let client = currentOrder.get_client();
				// let check = await this.check_credit_validation();
				if (this.env.pos.config.client_required_button ){
					if (client) {
						super.validateOrder(isForceValidate);

					}else {
						return self.showPopup('ErrorPopup',{
							'title': this.env._t('Empty Client'),
							'body': this.env._t('There must be Client in your order before it can be validated.'),
						});
					}
				}else {
					super.validateOrder(isForceValidate);

				}
			}
	};

	Registries.Component.extend(PaymentScreen, PaymentScreenWidget);

	return PaymentScreen;
});
