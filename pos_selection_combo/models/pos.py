# -*- coding: utf-8 -*-

from datetime import timedelta
from functools import partial

import pytz

from odoo import fields, models, api, _
from odoo.osv.expression import AND


class PosOrder(models.Model):
    _inherit = "pos.order"

    def _get_price_subtotal(self):
        for case in self:
            case.price_subtotal = sum([x.price_subtotal for x in case.lines if not x.is_combo_product])

    price_subtotal = fields.Float(compute=_get_price_subtotal, string="Subtotal")

    def _order_fields(self, ui_order):
        res = super(PosOrder, self)._order_fields(ui_order)

        process_line = partial(self.env['pos.order.line']._order_own_line_fields, session_id=ui_order['pos_session_id'], add_own_line=True)

        order_lines = [process_line(l) for l in ui_order['lines']] if ui_order['lines'] else False

        new_order_line = []
        for order_line in order_lines:
            flag = 1

            price_subtotal = 0
            price_subtotal_incl = 0
            # 'price_subtotal': 122.61, 'price_subtotal_incl': 141,

            if 'own_line' in order_line[2]:
                product = self.env['product.product'].search([('id', '=', order_line[2]['product_id'])])

                # print(order_line[2]['own_line'])
                # for line in order_line[2]['own_line']:
                #     line[2]['price_unit'] = line[2]['price']
                own_pro_list = [process_line(l) for l in order_line[2]['own_line']] if order_line[2]['own_line'] else False
                i = 1

                if own_pro_list:
                    master_line = own_pro_list[-1]

                    for own in own_pro_list:
                    # for own in own_pro_list[:-2]:

                        if not product.include_price and i != len(own_pro_list):
                            # flag = 0
                            i += 1
                            own[2]['price_subtotal'] = 0
                            own[2]['price_subtotal_incl'] = 0
                            # order_line[2]['price_subtotal'] -=own[2]['price_subtotal_incl']
                            # order_line[2]['price_subtotal_incl'] -=own[2]['price_subtotal_incl']
                        else:
                            flag = 0
                        # own[2]['price_unit'] = own[2]['price']

                        # if condition:
                        #     pass

                        new_order_line.append(own)

                    # new_order_line.append(master_line)
            # order_line[2]['price_subtotal'] -= price_subtotal_incl
            # order_line[2]['price_subtotal_incl'] -= price_subtotal_incl
            if flag:
                new_order_line.append(order_line)


        # for line in new_order_line:
        #     if not 'price_unit' in line[2]:
        #         print(line[2])
        #         line[2]['price_unit'] = line[2]['price']
        if new_order_line:
            print("SDASDASDASDASJKJKJJKJK")
            process_line = partial(self.env['pos.order.line']._order_line_fields, session_id=ui_order['pos_session_id'])
            print("SADASWW")
            print(process_line)
            order_lines = [process_line(l) for l in new_order_line]
            print("(((order_lines)))")
            print(order_lines)
            res['lines'] = order_lines
        print("(((((((((((((((((res)))))))))))))))))")
        print(res)
        return res


class pos_order_line(models.Model):
    _inherit = "pos.order.line"

    is_selection_combo = fields.Boolean("Selection Combo Line")
    own_ids = fields.One2many("pos.order.line.own", 'orderline_id', "Extra Toppings")
    # Mani added this field to segregate the actual products added as combo items from main item
    is_combo_product = fields.Boolean("combo Products")

    def _order_own_line_fields(self, line, session_id=None, add_own_line=False):
        own_line = []
        if line and 'own_line' in line[2] and add_own_line:
            own_line = line[2]['own_line']
        print('session_id',session_id)

        line = super(pos_order_line, self)._order_line_fields(line, session_id=session_id)

        if own_line:
            line[2]['own_line'] = own_line
        return line


class pos_order_line_own(models.Model):
    _name = "pos.order.line.own"
    _description = "POS Order Line own"

    orderline_id = fields.Many2one('pos.order.line', 'POS Line')
    product_id = fields.Many2one('product.product', 'Product')
    price = fields.Float('Item Price', required=True)
    qty = fields.Float('Quantity', default='1', required=True)

class ReportSaleDetails(models.AbstractModel):

    _inherit = 'report.point_of_sale.report_saledetails'


    @api.model
    def get_sale_details(self, date_start=False, date_stop=False, config_ids=False, session_ids=False):
        """ Serialise the orders of the requested time period, configs and sessions.

        :param date_start: The dateTime to start, default today 00:00:00.
        :type date_start: str.
        :param date_stop: The dateTime to stop, default date_start + 23:59:59.
        :type date_stop: str.
        :param config_ids: Pos Config id's to include.
        :type config_ids: list of numbers.
        :param session_ids: Pos Config id's to include.
        :type session_ids: list of numbers.

        :returns: dict -- Serialised sales.
        """
        domain = [('state', 'in', ['paid','invoiced','done'])]

        if (session_ids):
            domain = AND([domain, [('session_id', 'in', session_ids)]])
        else:
            if date_start:
                date_start = fields.Datetime.from_string(date_start)
            else:
                # start by default today 00:00:00
                user_tz = pytz.timezone(self.env.context.get('tz') or self.env.user.tz or 'UTC')
                today = user_tz.localize(fields.Datetime.from_string(fields.Date.context_today(self)))
                date_start = today.astimezone(pytz.timezone('UTC'))

            if date_stop:
                date_stop = fields.Datetime.from_string(date_stop)
                # avoid a date_stop smaller than date_start
                if (date_stop < date_start):
                    date_stop = date_start + timedelta(days=1, seconds=-1)
            else:
                # stop by default today 23:59:59
                date_stop = date_start + timedelta(days=1, seconds=-1)

            domain = AND([domain,
                [('date_order', '>=', fields.Datetime.to_string(date_start)),
                ('date_order', '<=', fields.Datetime.to_string(date_stop))]
            ])

            if config_ids:
                domain = AND([domain, [('config_id', 'in', config_ids)]])

        orders = self.env['pos.order'].search(domain)

        user_currency = self.env.company.currency_id

        total = 0.0
        products_sold = {}
        taxes = {}
        for order in orders:
            if user_currency != order.pricelist_id.currency_id:
                total += order.pricelist_id.currency_id._convert(
                    order.amount_total, user_currency, order.company_id, order.date_order or fields.Date.today())
            else:
                total += order.amount_total
            currency = order.session_id.currency_id
            order_tax = 0
            base_amount = 0
            for line in order.lines:
                key = (line.product_id, line.price_unit, line.discount)
                products_sold.setdefault(key, 0.0)
                products_sold[key] += line.qty

                # standard
                # if line.tax_ids_after_fiscal_position and not line.is_combo_product: # mani
                #     line_taxes = line.tax_ids_after_fiscal_position.compute_all(line.price_unit * (1-(line.discount or 0.0)/100.0), currency, line.qty, product=line.product_id, partner=line.order_id.partner_id or False)
                #     for tax in line_taxes['taxes']:
                #         taxes.setdefault(tax['id'], {'name': tax['name'], 'tax_amount':0.0, 'base_amount':0.0})
                #         taxes[tax['id']]['tax_amount'] += tax['amount']
                #         taxes[tax['id']]['base_amount'] += tax['base']
                #         order_tax += tax['amount']
                #         base_amount += tax['base']
                # else:
                #     if line.is_combo_product:
                #         continue
                #     taxes.setdefault(0, {'name': _('No Taxes'), 'tax_amount':0.0, 'base_amount':0.0})
                #     taxes[0]['base_amount'] += line.price_subtotal_incl

                # custom
                # if line.tax_ids_after_fiscal_position and not line.is_combo_product: # mani
                #     line_taxes = line.tax_ids_after_fiscal_position.compute_all(line.price_unit * (1-(line.discount or 0.0)/100.0), currency, line.qty, product=line.product_id, partner=line.order_id.partner_id or False)
                #     for tax in line_taxes['taxes']:
                #         #taxes.setdefault(tax['id'], {'name': tax['name'], 'tax_amount':0.0, 'base_amount':0.0})
                #         # taxes[tax['id']]['tax_amount'] += tax['amount']
                #         # taxes[tax['id']]['base_amount'] += tax['base']
                #         order_tax += tax['amount']
                #         base_amount += tax['base']
                # else:
                #     if line.is_combo_product:
                #         continue
                #     taxes.setdefault(0, {'name': _('No Taxes'), 'tax_amount':0.0, 'base_amount':0.0})
                #     taxes[0]['base_amount'] += line.price_subtotal_incl

            # updating lines
            tax_id = order.lines.mapped('tax_ids_after_fiscal_position')
            if tax_id.id not in taxes :
                taxes.setdefault(tax_id.id, {'name': tax_id.name, 'tax_amount': 0.0, 'base_amount': 0.0})
            if  tax_id.id or order.amount_tax:
                taxes[tax_id.id]['tax_amount'] += order.amount_tax
                taxes[tax_id.id]['base_amount'] += order.price_subtotal

            else:
                taxes[0]['base_amount'] += order.price_subtotal
                print(" order,,,,,,,,,,,,,", order.name, taxes[0]['base_amount'], order.price_subtotal)

            # if order_tax and round(order_tax,2) != round(order.amount_tax,2):
            #     print("Tax Difference ......", order.name, round(order_tax,2), round(order.amount_tax,2))
            #
            # if base_amount and round(base_amount,2) != round(round(order.amount_total,2) - round(order.amount_tax,2),2):
            #     print("Base Difference ......", order.name, round(base_amount,2), round(round(order.amount_total,2) - round(order.amount_tax,2),2))

        payment_ids = self.env["pos.payment"].search([('pos_order_id', 'in', orders.ids)]).ids
        if payment_ids:
            self.env.cr.execute("""
                SELECT method.name, sum(amount) total
                FROM pos_payment AS payment,
                     pos_payment_method AS method
                WHERE payment.payment_method_id = method.id
                    AND payment.id IN %s
                GROUP BY method.name
            """, (tuple(payment_ids),))
            payments = self.env.cr.dictfetchall()
        else:
            payments = []

        return {
            'currency_precision': user_currency.decimal_places,
            'total_paid': user_currency.round(total),
            'payments': payments,
            'company_name': self.env.company.name,
            'taxes': list(taxes.values()),
            'products': sorted([{
                'product_id': product.id,
                'product_name': product.name,
                'code': product.default_code,
                'quantity': qty,
                'price_unit': price_unit,
                'discount': discount,
                'uom': product.uom_id.name
            } for (product, price_unit, discount), qty in products_sold.items()], key=lambda l: l['product_name'])
        }
