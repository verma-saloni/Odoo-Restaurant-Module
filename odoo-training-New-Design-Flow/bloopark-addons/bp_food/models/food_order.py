import time

from odoo import _, api, fields, models
from odoo.exceptions import ValidationError
from odoo.osv import expression
from odoo.tools import DEFAULT_SERVER_DATETIME_FORMAT
from datetime import datetime, date

from odoo import models, fields, api


class FoodOrder(models.Model):
    _name = "food.order"
    _description = "Order window for the Restaurant from Menu"

    table = fields.Many2one('food.table', 'Choose Table')
    name = fields.Char(string='Order', copy=False,
                       readonly=True, index=True,
                       default=lambda self: 'New')
    capacity = fields.Integer("Capacity")
    order_date = fields.Date(string='Order Date', required=True)
    order_customer_id = fields.Many2one('res.partner', string='Name of Customer')
    order_dish_id = fields.Many2many('food.menu', string='Dish to be Ordered')
    order_dishprice = fields.Float(related='order_dish_id.dish_price')
    order_server = fields.Many2one('hr.employee', string='Server/Waiter Name')
    order_amount = fields.Float(string='Items Total', compute='_compute_total_price')
    quantity = fields.Integer('Quantity', required=True, default=1)
    order_comments = fields.Text('Add comments here for customisation or Allergies')

    @api.model
    def create(self, vals):
        if vals.get('name', 'New') == 'New':
            vals['name'] = self.env['ir.sequence'].next_by_code(
                'food.order') or 'New'
        result = super(FoodOrder, self).create(vals)
        return result

    @api.depends('dish_order_line.dish_price')
    def _bill_total(self):
        """
             To calculate the sum of the order
        """
        self.order_amount = 0
        for line in self:
            do = self.dish_order_line
            self.order_amount = self.order_amount + do.dish_price
        return self.order_amount

    @api.depends('order_dish_id', 'quantity')
    def _compute_total_price(self):
        for line in self:
            line.order_amount = line.quantity * line.order_dish_id.dish_price





