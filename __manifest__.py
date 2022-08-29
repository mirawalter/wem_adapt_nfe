# -*- coding: utf-8 -*-

{
    'name' : 'Adaptação de rotinas NFe',
    'author' : 'Walter E. Miranda',
    'version': '1.0',
    'category': 'Accounting',
    'depends' : ['base', 'l10n_br_nfe_spec', 'l10n_br_nfe'],

    'description': """
Módulo brasileiro para adaptação de rotinas de emissão de nota fiscal.
===============================================

Adapta e melhora o processo de emissão de nota fiscal dos módulos l10n_br. Torna diversos campos mais intuitivos no preenchimento.
    """,
    "data": [
        "view/account_move.xml"]
    'installable': True,
    'auto_install': False,
}
