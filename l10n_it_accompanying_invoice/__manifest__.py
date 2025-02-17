# Copyright 2017 Lorenzo Battistini - Agile Business Group
# Copyright 2020 Simone Vanin - Agile Business Group
# Copyright 2023 Simone Rubino - Aion Tech
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

{
    "name": "ITA - Fattura accompagnatoria",
    "summary": "Stampa della fattura accompagnatoria",
    "version": "16.0.1.0.1",
    "category": "Accounting",
    "website": "https://github.com/OCA/l10n-italy"
    "/tree/16.0/l10n_it_accompanying_invoice",
    "author": "Agile Business Group, " "Odoo Community Association (OCA)",
    "license": "AGPL-3",
    "application": False,
    "installable": True,
    "depends": [
        "l10n_it_delivery_note",
    ],
    "data": [
        "views/account.xml",
        "views/report_invoice.xml",
    ],
    # "external_dependencies": {
    #     "python": [
    #         "openupgradelib",
    #     ],
    # },
    # "pre_init_hook": "pre_absorb_old_module",
}
