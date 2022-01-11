import time

from odoo import _, api, fields, models
from odoo.exceptions import ValidationError
from odoo.osv import expression
from odoo.tools import DEFAULT_SERVER_DATETIME_FORMAT

from odoo import models, fields, api


class EmployeesType(models.Model):
    _name = "food.employeestype"
    _description = "Suggest New Employees or Jobs for the Restaurant"

    name = fields.Char(string='New Job')
    occupation_type = fields.Selection([
        ('waiter', 'Waiter'),
        ('accountant', 'Accountant'),
        ('manager', 'Manager'),
        ('maintenance', 'Maintenance'),
        ('chef', 'Chef')], string='Occupation of the Person in the Restaurant?')

    comments = fields.Char(string="Add Comments about the job role")
