odoo.define('am_pos_delivery_company.ControlButtons', function (require) {
    'use strict';

    const PosComponent = require('point_of_sale.PosComponent');
    const ProductScreen = require('point_of_sale.ProductScreen');
    const Registries = require('point_of_sale.Registries');
    const { useListener } = require('web.custom_hooks');

    class TheChefzButton extends PosComponent {
        constructor() {
            super(...arguments);
            useListener('click', this._onClick);
        }
        _onClick() {
          var self = this;
          var order = self.env.pos.get_order();
          var partner = self.env.pos.partners.filter(method => method.name.toLowerCase() == 'the chefz');
          if (partner.length == 0 ) {
            self.showPopup('ErrorPopup',{
  						'title': this.env._t('Client Not Found'),
  						'body': this.env._t('There is no customer by name "The Chefz".'),
  					});
          }else if (partner.length > 1) {
            self.showPopup('ErrorPopup',{
  						'title': this.env._t('Client Error'),
  						'body': this.env._t('There are many clients with the same name "The Chefz".'),
  					});
          }else {
            order.set_client(self.env.pos.db.get_partner_by_id(partner[0].id));
          }
        }
    }
    TheChefzButton.template = 'am_pos_delivery_company.TheChefzButton';

    ProductScreen.addControlButton({
        component: TheChefzButton,
        condition: function () {
            return this.env.pos.config.TheChefz;
        },
    });

    Registries.Component.add(TheChefzButton);

    class MrsoolButton extends PosComponent {
        constructor() {
            super(...arguments);
            useListener('click', this._onClick);
        }
        _onClick() {
          var self = this;
          var order = self.env.pos.get_order();
          var partner = self.env.pos.partners.filter(method => method.name.toLowerCase() == 'mrsool');
          if (partner.length == 0 ) {
            self.showPopup('ErrorPopup',{
  						'title': this.env._t('Client Not Found'),
  						'body': this.env._t('There is no customer by name "Mrsool".'),
  					});
          }else if (partner.length > 1) {
            self.showPopup('ErrorPopup',{
  						'title': this.env._t('Client Error'),
  						'body': this.env._t('There are many clients with the same name "Mrsool".'),
  					});
          }else {
            order.set_client(self.env.pos.db.get_partner_by_id(partner[0].id));
          }
        }
    }
    MrsoolButton.template = 'am_pos_delivery_company.MrsoolButton';

    ProductScreen.addControlButton({
        component: MrsoolButton,
        condition: function () {
            return this.env.pos.config.Mrsool;
        },
    });

    Registries.Component.add(MrsoolButton);

    class ToyoButton extends PosComponent {
        constructor() {
            super(...arguments);
            useListener('click', this._onClick);
        }
        _onClick() {
          var self = this;
          var order = self.env.pos.get_order();
          var partner = self.env.pos.partners.filter(method => method.name.toLowerCase() == 'toyo');
          if (partner.length == 0 ) {
            self.showPopup('ErrorPopup',{
              'title': this.env._t('Client Not Found'),
              'body': this.env._t('There is no customer by name "TOYO".'),
            });
          }else if (partner.length > 1) {
            self.showPopup('ErrorPopup',{
              'title': this.env._t('Client Error'),
              'body': this.env._t('There are many clients with the same name "TOYO".'),
            });
          }else {
            order.set_client(self.env.pos.db.get_partner_by_id(partner[0].id));
          }
        }
    }
    ToyoButton.template = 'am_pos_delivery_company.ToyoButton';

    ProductScreen.addControlButton({
        component: ToyoButton,
        condition: function () {
            return this.env.pos.config.Toyo;
        },
    });

    Registries.Component.add(ToyoButton);

    class TrkerButton extends PosComponent {
        constructor() {
            super(...arguments);
            useListener('click', this._onClick);
        }
        _onClick() {
          var self = this;
          var order = self.env.pos.get_order();
          var partner = self.env.pos.partners.filter(method => method.name.toLowerCase() == 'trker');
          if (partner.length == 0 ) {
            self.showPopup('ErrorPopup',{
              'title': this.env._t('Client Not Found'),
              'body': this.env._t('There is no customer by name "Trker".'),
            });
          }else if (partner.length > 1) {
            self.showPopup('ErrorPopup',{
              'title': this.env._t('Client Error'),
              'body': this.env._t('There are many clients with the same name "Trker".'),
            });
          }else {
            order.set_client(self.env.pos.db.get_partner_by_id(partner[0].id));
          }
        }
    }
    TrkerButton.template = 'am_pos_delivery_company.TrkerButton';

    ProductScreen.addControlButton({
        component: TrkerButton,
        condition: function () {
            return this.env.pos.config.Trker;
        },
    });

    Registries.Component.add(TrkerButton);


    class HungerStationButton extends PosComponent {
        constructor() {
            super(...arguments);
            useListener('click', this._onClick);
        }
        _onClick() {
          var self = this;
          var order = self.env.pos.get_order();
          var partner = self.env.pos.partners.filter(method => method.name.toLowerCase() == 'hunger station');
          if (partner.length == 0 ) {
            self.showPopup('ErrorPopup',{
              'title': this.env._t('Client Not Found'),
              'body': this.env._t('There is no customer by name "Hunger Station".'),
            });
          }else if (partner.length > 1) {
            self.showPopup('ErrorPopup',{
              'title': this.env._t('Client Error'),
              'body': this.env._t('There are many clients with the same name "Hunger Station".'),
            });
          }else {
            order.set_client(self.env.pos.db.get_partner_by_id(partner[0].id));
          }
        }
    }
    HungerStationButton.template = 'am_pos_delivery_company.HungerStationButton';

    ProductScreen.addControlButton({
        component: HungerStationButton,
        condition: function () {
            return this.env.pos.config.HungerStation;
        },
    });

    Registries.Component.add(HungerStationButton);

    class JahezButton extends PosComponent {
        constructor() {
            super(...arguments);
            useListener('click', this._onClick);
        }
        _onClick() {
          var self = this;
          var order = self.env.pos.get_order();
          var partner = self.env.pos.partners.filter(method => method.name.toLowerCase() == 'jahez');
          if (partner.length == 0 ) {
            self.showPopup('ErrorPopup',{
              'title': this.env._t('Client Not Found'),
              'body': this.env._t('There is no customer by name "Jahez".'),
            });
          }else if (partner.length > 1) {
            self.showPopup('ErrorPopup',{
              'title': this.env._t('Client Error'),
              'body': this.env._t('There are many clients with the same name "Jahez".'),
            });
          }else {
            order.set_client(self.env.pos.db.get_partner_by_id(partner[0].id));
          }
        }
    }
    JahezButton.template = 'am_pos_delivery_company.JahezButton';

    ProductScreen.addControlButton({
        component: JahezButton,
        condition: function () {
            return this.env.pos.config.Jahez;
        },
    });

    Registries.Component.add(JahezButton);


    // return CategorySummaryButton;
});
