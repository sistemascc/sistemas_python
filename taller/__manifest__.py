# -*- coding: utf-8 -*-
{
    'name': "Gestion Taller",

    'summary': """
        Gestion Vehiculos y Reparaciones 
        """,

    'description': """
        Gestion vehiculos Y Reparaciones
    """,

    'author': "Praxya Formaplus",
    'website': "http://www.praxyaformaplus.com",
    'category': 'Gestion Vehiculo',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        "data/data.xml",
        "security/ir.model.access.csv",
        "views/vehiculo_view.xml",
        "views/order_reparacion_view.xml",

    ],

}
