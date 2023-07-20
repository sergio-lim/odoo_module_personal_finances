from odoo import api, fields, models

class FinancesJournal(models.Model):
    _name = "finances.journal"
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = "Finances Journal"

    # the convention name_id means is a many2one field
    entry_id = fields.Many2one('finances.entry', string="Registro")


