from odoo import models, fields, api, _
from datetime import datetime

class AccountMove(models.Model):
    _inherit = 'account.move'

    name = fields.Char(string="Number", readonly=True, copy=False, 
                       default=lambda self: _('NEW'))

    @api.model
    def create(self, vals):
        user = self.env.user
        branch_code = user.branch_id.name if user.branch_id else 'BRANCH-CODE'
        date = datetime.today().strftime('%y/%m')

        # Pilih sequence berdasarkan jenis transaksi
        if vals.get('move_type') == 'out_invoice':  # Invoice
            sequence_code = 'sequence.account.move.invoice'
            prefix = f"INV/{branch_code}/{date}/"
        elif vals.get('move_type') == 'in_invoice':  # Bills
            sequence_code = 'sequence.account.move.bills'
            prefix = f"BILLS/{branch_code}/{date}/"
        else:  # Journal Entries
            journal = self.env['account.journal'].browse(vals.get('journal_id'))
            journal_code = journal.code if journal else 'JRN'
            sequence_code = 'sequence.account.move.journal'
            prefix = f"{journal_code}/{branch_code}/{date}/"

        # Ambil nomor sequence
        sequence_number = self.env['ir.sequence'].next_by_code(sequence_code)
        if not sequence_number:
            sequence_number = '666'  

        vals['name'] = f"{prefix}{sequence_number}"

        return super(AccountMove, self).create(vals)
