# -*- coding: utf-8 -*-

from odoo import models, fields, api


class ResPartner(models.Model):
    _inherit = 'res.partner'
    _description = 'Partner inheritence for Customers that come to Restaurant'


    orientation = fields.Selection([
        ('vegan', 'Vegan'),
        ('veg', 'Vegetarian'),
        ('pesca', 'Pescatarian'),
        ('non_veg', 'Non-Vegetarian'),
    ], string='Veg/Non-Veg', default='non_veg')

    frequency = fields.Selection([
        ('freq', 'Frequent'),
        ('intermed', 'Intermediate'),
        ('rare', 'Rare'),
        ('first', 'First Time'),
        ], string='Frequency', default='first')
