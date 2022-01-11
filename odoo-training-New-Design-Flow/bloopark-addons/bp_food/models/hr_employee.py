import time

from odoo import _, api, fields, models
from odoo.exceptions import ValidationError
from odoo.osv import expression
from odoo.tools import DEFAULT_SERVER_DATETIME_FORMAT

from odoo import models, fields, api


class HrEmployee(models.Model):
    _inherit = 'hr.employee'
    _description = "Employee Details"

    occupation = fields.Many2one('food.employeestype', string='Occupation Type',
                                    ondelete='set null')




    category_ids = fields.Many2many(
        'hr.employee.category', 'student_category_rel',
        'student_id', 'category_id',
        string='Tags')
