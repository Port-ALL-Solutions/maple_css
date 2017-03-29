# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'Maple css',
    'category': 'Maple-Vertical',
    'version': '1.0',
    'author': "Portall Solution inc.",
    'website': "portall.ca",
    'summary': 'css for Maple Modules.',
    'description':
        """
css to allow layout customization
================================================

This module provides only dependecies.
        """,
    'depends': [
        'maple',
    ],
    'data': [
        'views/maple_asset.xml'
    ],
    'qweb': [
#        "static/src/xml/*.xml",
    ],
#    'bootstrap': True,  # load translations for login screen
    'installable': True,
    'application': False,
    'auto_install': False,
}

