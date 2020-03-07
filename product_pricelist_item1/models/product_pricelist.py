# -*- coding: utf-8 -*-

from odoo import api, models, fields, exceptions


class ProductPricelistItem(models.Model):
    _inherit = 'product.pricelist.item'

    price_with_discount = fields.Float(
        string="Precio + descuento")
