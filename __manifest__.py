# -*- coding: utf-8 -*-
{
    'name': "ipmanager",

    'summary': """
        App for managing IP address""",

    'description': """
        Long description of module's purpose
    """,

    'author': "Walter Tosolini",
    'website': "https://tosolini.info",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/12.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/group.xml',
        'security/ir.model.access.csv',
        'views/vlan.xml',
        'views/ipaddress.xml',
        'views/network.xml',
        'views/menu.xml',
        # 'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}