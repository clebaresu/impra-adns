# -*- coding: utf-8 -*-
{
    'name': 'Parar las alertas de soporte',
    'version': '1.0',
    'category': '',
    "sequence": 14,
    'complexity': "easy",
    'category': 'Hidden',
    'description': """
        Retira el mensaje de erp no soportado.
    """,
    'author': 'basado en el addon de Ruchir Shukla',
    'website': 'www.bizzappdev.com',
    'depends': ["mail",'web'],
    'init_xml': [],
    'data': [
        "base_view.xml",
        "mail_data.xml",
    ],
    'demo_xml': [],
    'test': [
    ],
    'qweb' : [
        "static/src/xml/base.xml",
    ],
    'installable': True,
    'auto_install': True,
}
# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
