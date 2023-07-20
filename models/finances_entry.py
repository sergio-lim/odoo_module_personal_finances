from odoo import api, fields, models

class FinancesEntry(models.Model):
    _name = "finances.entry"
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = "Finances Entry"


    date = fields.Date(string='Fecha', tracking=True)
    # tracking=True means everytime the record is changed the system will output a message telling what changed
    name = fields.Char(string='Nota', tracking=True)
    amount = fields.Integer(string='Cantidad', tracking=True)
    currency = fields.Selection([('cup', 'CUP'), ('mlc', 'MLC'), ('usd', 'USD'), ('btc', 'BTC')], string="Moneda")
    transaction = fields.Selection([('efectivo', 'Efectivo'), ('transferencia', 'Transferencia')], string="Tipo de Transaccion", tracking=True)
    type = fields.Selection([('entrada', 'Entrada'), ('salida', 'Salida')], string="Tipo", tracking=True)
    starred = fields.Boolean(string="Importante", tracking=True)
    # odoo understands active field as to archive or not
    active = fields.Boolean(string="Active", default=True)
