# -*- coding: utf-8 -*-

from odoo import api, models, fields, exceptions


class Vehicle(models.Model):
    _name = 'taller.vehiculo'
    # _rec_name = 'name'
    _description = 'Gestion Vehiculos Odoo'

    name = fields.Char(string="Name", help="Introduce el nombre", size=20,
                       defaul="Nuevo")
    active = fields.Boolean(string="Active", default=True)
    matricula = fields.Char("Placa")

    # Trabajando Restricciones en Odoo(sql_constraints)
    _sql_constraints = [
        ('vehiculo_name_uniq',
         'unique (name)',
         'Nombre tiene que ser unico.')
    ]

    tag_ids = fields.Many2many(
        comodel_name="vehiculo.tag"
    )

    # Trabajando con Restricciones en Odoo (Matricula)
    @api.constrains('matricula')
    def _check_matricula(self):
        # comprobamos que sea unica
        domain = [
            "|",
            ('matricula', '=', self.matricula),
            ('id', '!=', self.id),
        ]
        vehiculos = self.search(domain)
        if vehiculos:
            raise exceptions.ValidationError("Matricula duplicada")


class VehiculoTag(models.Model):
    _name = "vehiculo.tag"

    name = fields.Char(string="Name")


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
