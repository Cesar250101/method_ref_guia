# -*- coding: utf-8 -*-
{
    'name': "method_ref_guia",

    'summary': """
        Facturación desde el pedido de venta y pasa las guías de despacho como documento
        de referencia a la factura""",

    'description': """
        Facturación desde el pedido de venta y pasa las guías de despacho como documento
        de referencia a la factura
    """,

    'author': "Method ERP SpA",
    'website': "https://www.method.cl",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/12.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','l10n_cl_fe','l10n_cl_stock_picking'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}