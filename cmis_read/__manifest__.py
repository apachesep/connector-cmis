# -*- coding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    This module copyright (C) 2014 Savoir-faire Linux
#    (<http://www.savoirfairelinux.com>).
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

{
    'name': 'CMIS Read',
    'version': '7.0.1.0.0',
    'category': 'Knowledge Management',
    'summary': 'Store Document File from a Remote CMIS Server',
    'description': """
======================================
Attach files from a remote CMIS Server
======================================

This module allows you to use the CMIS backend to search in the DMS repository
and attach documents to OpenERP records.

Installation
============

You need to install the CMIS python library:

 pip install cmislib

Configuration
=============

Create a new CMIS backend with the host, login and password.

Usage
=====

* On one OpenERP record, click "Add from DMS".
* Type your query and then click on "Search".
* Filter your results if necessary
* Select the documents you want to attach
* Selected documents will be enqueued for importing

Contributors
------------

* El Hadji Dem (elhadji.dem@savoirfairelinux.com)
* Maxime Chambreuil (maxime.chambreuil@savoirfairelinux.com)
""",
    'author': 'Savoir-faire Linux, Odoo Community Association (OCA)',
    'website': 'www.savoirfairelinux.com',
    'license': 'AGPL-3',
    'depends': [
        'document',
        'cmis'
    ],
    'data': [
        'security/ir.model.access.csv',
        'wizard/ir_attachment_dms_view.xml',
    ],
    'js': [
        'static/src/js/document.js'
    ],
    'qweb': [
        'static/src/xml/document.xml'
    ],
    'test': [],
    'demo': [
    ],
    'installable': False,
    'auto_install': False,
}
