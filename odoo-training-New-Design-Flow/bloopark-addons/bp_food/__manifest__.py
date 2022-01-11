# -*- coding: utf-8 -*-
{
    'name': "bp_food",

    'summary': """
        Restaurant Module with customisations
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        Long description of module's purpose
    """,

    'author': "Saloni",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work incorrectly
    'depends': [
        'base',
        'hr',
        'sale',
    ],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'data/data.xml',
        'views/food_customer_view.xml',
        'views/food_employee_view.xml',
        'wizards/suggestion_wizard_view.xml',
        'views/food_menu_view.xml',
        'views/food_order_view.xml',
        'views/food_table_view.xml',
        'views/food_dishtype_view.xml',
        'views/food_employeestype_view.xml',
        'views/food_calendar.xml',

    ],
    # only loaded in demonstration mode
    'demo': [],
}
