from odoo import _, api, fields, models
from odoo.exceptions import ValidationError


class SaleOrder(models.Model):
    _inherit = "sale.order"

    x_total_lines = fields.Integer(
        string=_("Total de Líneas de Pedido"),
        compute="_compute_x_total_lines",
        store=True,
    )

    @api.depends("order_line")
    def _compute_x_total_lines(self):
        for order in self:
            order.x_total_lines = len(
                order.order_line.filtered(lambda line: not line.display_type)
            )

    @api.constrains("x_total_lines")
    def _check_x_total_lines(self):
        for record in self:
            if record.x_total_lines < 0:
                raise ValidationError(
                    _("El total de líneas no puede ser un valor negativo.")
                )
