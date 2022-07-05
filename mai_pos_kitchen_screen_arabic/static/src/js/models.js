odoo.define("mai_pos_kitchen_screen_arabic.models", function (require) {
"use strict";

var models = require('point_of_sale.models');
var multi_print = require('pos_restaurant.multiprint');
var core = require('web.core');
var Printer = require('point_of_sale.Printer').Printer;

var QWeb = core.qweb;

models.load_fields('res.company', ['street','street2','city','state_id','vat']);
models.load_fields('res.partner', ['unique_code']);
models.load_fields('product.product',['name','name_arabic']);

var _super_order = models.Order.prototype;
models.Order = models.Order.extend({
  build_line_resume: function(){
      var resume = {};
      this.orderlines.each(function(line){
          if (line.mp_skip) {
              return;
          }
          var line_hash = line.get_line_diff_hash();
          var qty  = Number(line.get_quantity());
          var note = line.get_note();
          var product_id = line.get_product().id;
          if (typeof resume[line_hash] === 'undefined') {
              resume[line_hash] = {
                  qty: qty,
                  note: note,
                  product_id: product_id,
                  order_menu: line.order_menu,
                  product_name_wrapped: line.generate_wrapped_product_name(),
              };
          } else {
              resume[line_hash].qty += qty;
          }

      });
      return resume;
  },

  computeChanges: function(categories){
    var self = this;
    // const res = _super_order.computeChanges.apply(this, arguments);
    var current_res = this.build_line_resume();
    var old_res     = this.saved_resume || {};
    var json        = this.export_as_JSON();
    var add = [];
    var rem = [];
    var line_hash;

    for ( line_hash in current_res) {
        var curr = current_res[line_hash];
        var old  = {};
        var found = false;
        for(var id in old_res) {
            if(old_res[id].product_id === curr.product_id){
                found = true;
                old = old_res[id];
                break;
            }
        }

        var product = this.pos.db.get_product_by_id(curr.product_id);
        if (!found) {
            add.push({
                'id':       curr.product_id,
                'name':     product.display_name,
                'name_arabic':     product.name_arabic,
                'order_menu': curr.order_menu,
                'is_selection_combo_product': product.is_selection_combo,
                'name_wrapped': curr.product_name_wrapped,
                'note':     curr.note,
                'qty':      curr.qty,
            });
        } else if (old.qty < curr.qty) {
            add.push({
                'id':       curr.product_id,
                'name':     product.display_name,
                'name_arabic':     product.name_arabic,
                'order_menu': curr.order_menu,
                'is_selection_combo_product': product.is_selection_combo,
                'name_wrapped': curr.product_name_wrapped,
                'note':     curr.note,
                'qty':      curr.qty - old.qty,
            });
        } else if (old.qty > curr.qty) {
            rem.push({
                'id':       curr.product_id,
                'name':     product.display_name,
                'name_arabic':     product.name_arabic,
                'order_menu': curr.order_menu,
                'is_selection_combo_product': product.is_selection_combo,
                'name_wrapped': curr.product_name_wrapped,
                'note':     curr.note,
                'qty':      old.qty - curr.qty,
            });
        }
    }

    for (line_hash in old_res) {
        var found = false;
        for(var id in current_res) {
            if(current_res[id].product_id === old_res[line_hash].product_id)
                found = true;
        }
        if (!found) {
            var old = old_res[line_hash];
            var product = this.pos.db.get_product_by_id(old.product_id);
            rem.push({
                'id':       old.product_id,
                'name':     product.display_name,
                'name_arabic':     product.name_arabic,
                'order_menu': old.order_menu,
                'is_selection_combo_product': product.is_selection_combo,
                'name_wrapped': old.product_name_wrapped,
                'note':     old.note,
                'qty':      old.qty,
            });
        }
    }

    if(categories && categories.length > 0){
        // filter the added and removed orders to only contains
        // products that belong to one of the categories supplied as a parameter

        var self = this;

        var _add = [];
        var _rem = [];

        for(var i = 0; i < add.length; i++){
            if(self.pos.db.is_product_in_category(categories,add[i].id)){
                _add.push(add[i]);
            }
        }
        add = _add;

        for(var i = 0; i < rem.length; i++){
            if(self.pos.db.is_product_in_category(categories,rem[i].id)){
                _rem.push(rem[i]);
            }
        }
        rem = _rem;
    }

    var d = new Date();
    var hours   = '' + d.getHours();
        hours   = hours.length < 2 ? ('0' + hours) : hours;
    var minutes = '' + d.getMinutes();
        minutes = minutes.length < 2 ? ('0' + minutes) : minutes;
    // console.log("WWWWW");
    // console.log({
    //   'pos': self.pos,
    //   'new': add,
    //   'cancelled': rem,
    //   'table': json.table || false,
    //   'floor': json.floor || false,
    //   'name': json.name  || 'unknown order',
    //   'time': {
    //       'hours':   hours,
    //       'minutes': minutes,
    //   },
    // });
    return {
      'pos': self.pos,
      'new': add,
      'cancelled': rem,
      'table': json.table || false,
      'floor': json.floor || false,
      'name': json.name  || 'unknown order',
      'time': {
          'hours':   hours,
          'minutes': minutes,
      },
    };

  },

  printChanges: async function(){
      var printers = this.pos.printers;
      let isPrintSuccessful = true;
      for(var i = 0; i < printers.length; i++){
          var changes = this.computeChanges(printers[i].config.product_categories_ids);
          if ( changes['new'].length > 0 || changes['cancelled'].length > 0){
              var receipt = QWeb.render('OrderChangeReceipt',{changes:changes, widget:this});
// console.log("AAAA");
// console.log(receipt);
// console.log(printers[i]);
              const result = await printers[i].print_receipt(receipt);
              if (!result.successful) {
                  isPrintSuccessful = false;
              }
          }
      }
      return isPrintSuccessful;
  },


});


})
