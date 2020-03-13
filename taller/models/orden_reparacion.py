# -*- coding: utf-8 -*-

from odoo import api, models, fields, exceptions


class OrderReparacion(models.Model):
    _name = 'taller.orden.reparacion'
    _description = 'Gestion Ordenes Reparacion'

    state = fields.Selection([
        ('nuevo', 'Nuevo'),
        ('confirmado', 'Confirmado'),
        ('realizado', 'Realizado'),
        ('cancelado', 'Cancelado')
    ], string='Estado', readonly=True, index=True, copy=False,
        default='draft', tracking=True)

    active = fields.Boolean(string="Active", default=True)
    name = fields.Char(
        string="Name",
        help="Introduce el nombre",
        default="Nueva Orden Raparacion")
    partner_id = fields.Many2one(
        comodel_name="res.partner", string="Cliente")

    reparacion_line_ids = fields.One2many(
        comodel_name="taller.orden.reparacion.line",
        inverse_name="reparacion_id",
        string="lineas Reparacion"
    )

    notas = fields.Html(string="Notas")

    READONLY_STATES = {
        'nuevo': [('readonly', False)],
        'confirmado': [('readonly', True)],
        'cancelado': [('readonly', False)],
    }

    company_id = fields.Many2one('res.company', 'Company', required=True,
                                 index=True, states=READONLY_STATES,
                                 default=lambda self: self.env.company.id)

    @api.model
    def create(self, vals):
        new_seq_name = self.env['ir.sequence'].next_by_code(
            'orden.reparacion') or 'New'
        vals.update(name=new_seq_name)
        res = super(OrderReparacion, self).create(vals)
        return res

    def confirm(self):
        self.write({'state': "confirmado"})





    class OrderReparacionLine(models.Model):
        _name = 'taller.orden.reparacion.line'

        active = fields.Boolean(string="Active", default=True)
        name = fields.Char(
            string="Name",
            help="Introduce el nombre",
            default="Nueva Linea Raparacion")
        reparacion_id = fields.Many2one(comodel_name="taller.orden.reparacion")
        vehiculo_id = fields.Many2one(
            comodel_name="taller.vehiculo", string="Vehiculo")


"""
    class VehicleInherit(models.Model):

        _inherit = 'taller.vehiculo' #Voy a heredar del modelo taller.vehiculo

        marca = fields.Char("Marca")

"""
"""
Nota: Si se desea Clonar se ocupa el:
 _name = 'taller.vehiculo.copia' #Todos lo que le agregue al nuevo modelo almacenalo en la misma

En caso contrario de deja la herencia como esta con el _inherit

"""

# class taller(models.Model):
#     _name = 'taller.taller'
#     _description = 'taller.taller'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
