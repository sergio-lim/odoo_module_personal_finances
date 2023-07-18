from odoo import api, fields, models

class FinancesEntry(models.Model):
    _name = "finances.entry"
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = "Finances Entry"


    date = fields.Date(string='Fecha')
    description = fields.Char(string='Nota')
    amount = fields.Integer(string='Cantidad')
    currency = fields.Selection([('cup', 'CUP'), ('mlc', 'MLC'), ('usd', 'USD'), ('btc', 'BTC')], string="Moneda")
    transaction = fields.Selection([('efectivo', 'Efectivo'), ('transferencia', 'Transferencia')], string="Tipo de Transaccion")
    type = fields.Selection([('entrada', 'Entrada'), ('salida', 'Salida')], string="Tipo")
    starred = fields.Boolean(string="Importante")
    # odoo understands active field as to archive or not
    active = fields.Boolean(string="Active", default=True)
