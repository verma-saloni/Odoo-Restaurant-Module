import time

from odoo import _, api, fields, models
from odoo.exceptions import ValidationError
from odoo.osv import expression
from odoo.tools import DEFAULT_SERVER_DATETIME_FORMAT

from odoo import models, fields, api


class RestDish(models.Model):
    _name = "food.menu"
    _description = "Menu Details and Dishes"

    name = fields.Char("Name of Dish", required=True)
    dish_details = fields.Many2one('food.dishtype', string='Dish Details',
                                    ondelete='set null')

    dish_type = fields.Selection([
        ('veg', 'Vegetarian'),
        ('nonveg', 'Non-Vegetarian'),
        ('mix', 'Mixed')], string='Type of Dish')
    dish_price = fields.Float(string='Price of the Dish')
    dish_cuisine = fields.Char(string='Cuisine it belongs to')
    dish_comments = fields.Char(string='Add Comments about Dish')
    status = fields.Selection(string='Status', selection=[
        ('open', 'Open'),
        ('in_progress', 'In Progress'),
        ('finished', 'Finished'),
    ], default='open', required=True)