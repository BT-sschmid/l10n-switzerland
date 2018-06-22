##############################################################################
#
#    Swiss localization Direct Debit module for Odoo
#    Copyright (C) 2014 Compassion (http://www.compassion.ch)
#    @author: Cyril Sester <cyril.sester@outlook.com>
#
#    This module has been inspired by the SEPA Direct Debit module
#    (by Alexis de Lattre)
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
    'name': 'LSV and Postfinance Direct Debit file generation',
    'summary': 'Create LSV and Direct Debit (postfinance) files',
    'version': '8.0.1.0.0',
    'license': 'AGPL-3',
    'author': "Compassion,Odoo Community Association (OCA)",
    'website': 'http://www.compassion.ch',
    'category': 'Localization',
    'depends': ['account',
                'account_direct_debit',
                'account_banking_mandate',
                'account_banking_payment_export',
                'account_payment',
                'l10n_ch_payment_slip',
                'l10n_ch_payment_slip_base_transaction_id'],
    'external_dependencies': {},
    'data': [
        'data/payment_type.xml',
        'data/export_filename_sequence.xml',
        'data/schedulers.xml',
        'data/dd_email_template.xml',
        'data/lsv_email_template.xml',
        'view/banking_export_ch_dd_view.xml',
        'view/bank_view.xml',
        'view/dd_export_wizard_view.xml',
        'view/lsv_export_wizard_view.xml',
        'view/payment_order_view.xml',
        'view/invoice_view.xml',
        'view/account_banking_mandate_view.xml',
        'view/company_view.xml',
        'view/partner_view.xml',
        'view/lsv_dd_error_view.xml',
        'security/ir.model.access.csv',
    ],
    'demo': [],
    'test': [
        'test/lsv-dd-test.yml',
    ],
    'auto_install': False,
    'installable': True,
}
