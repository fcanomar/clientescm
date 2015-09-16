# -*- coding: utf-8 -*-
{
    'name': "Gestión de la relación con el cliente",

    'summary': """
        Funcionalidades para clientes""",

    'description': """
        NIF único (solo si no hay duplicados al instalarlo),
        nuevos Campos ficha clientes,
        población en la vista lista
        ...
    """,

    'author': "Your Company",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/openerp/addons/base/module/module_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','crm'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'clientcm_form.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo.xml',
    ],
}