# -*- coding: utf-8 -*-

from odoo import api, fields, models, _
#from odoo.exceptions import UserError, AccessError
from odoo.osv import expression

class DetPag(models.AbstractModel):
    _name = 'nfe.40.detpag'
    _inherit = 'spec.mixin.nfe'
    _generateds_type = 'detPagType'
    wem_formapagamento = fields.Selection([
        ('dinheiro', 'Dinheiro'),
        ('cheque', 'Cheque'),
        ('cartaocredito', 'Cartão de Crédito'),
        ('cartaodebito', 'Cartão de Débito'),
        ('creditoloja', 'Crédito Loja'),
        ('valealimentacao', 'Vale Alimentação'),
        ('valerefeicao', 'Vale Refeição'),
        ('valepresente', 'Vale Presente'),
        ('valecombustivel', 'Vale Combustível'),
        ('outros', 'Outros')
        ], 'Forma de pagamento', required=True)
    wem_avistaouaprazo = fields.Selection([
        ('avista', 'À vista'),
        ('aprazo', 'À prazo')], readonly="True", required="True")
    nfe40_tPag = fields.Char(
        string="Forma de Pagamento Selecionada", xsd_required=True,
        xsd_type="tPagType", compute='_compute_formapagamentonfe', readonly="True")

def _compute_formapagamentonfe(self):
    if self.wem_formapagamento == 'dinheiro':
        self.nfe40_tPag = '01'
    if self.wem_formapagamento == 'cheque':
        self.nfe40_tPag = '02'
    if self.wem_formapagamento == 'cartaocredito':
        self.nfe40_tPag = '03'
    if self.wem_formapagamento == 'cartaodebito':
        self.nfe40_tPag = '04'
    if self.wem_formapagamento == 'creditoloja':
        self.nfe40_tPag = '05'
    if self.wem_formapagamento == 'valealimentacao':
        self.nfe40_tPag = '10'
    if self.wem_formapagamento == 'valerefeicao':
        self.nfe40_tPag = '11'
    if self.wem_formapagamento == 'valepresente':
        self.nfe40_tPag = '12'
    if self.wem_formapagamento == 'valecombustivel':
        self.nfe40_tPag = '13'
    if self.wem_formapagamento == 'outros':
        self.nfe40_tPag = '99'

def _compute_avistaouaprazo(self):
    if self.wem_avistaouaprazo == 'avista':
        self.nfe40_indPag = [01]
    if self.wem_avistaouaprazo == 'aprazo':
        self.nfe40_indPag = [02]
