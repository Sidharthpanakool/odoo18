# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import _, fields, models
from odoo.exceptions import UserError, ValidationError


class StockPicking(models.Model):
    _inherit = "stock.picking"

    def button_validate(self):
        today=fields.Datetime.today()
        res = super().button_validate()
        stock_move_line=self.env['stock.move.line'].search_read([('product_id','=',self.product_id.id),('picking_id','=',self.id)],['expiration_date'])
        stock_move_line=stock_move_line[0]
        stock_move_line=stock_move_line['expiration_date']
        print("Aa", stock_move_line)
        if stock_move_line<today:
            raise ValidationError(_("Product Already Expired"))
        else:
            return res



