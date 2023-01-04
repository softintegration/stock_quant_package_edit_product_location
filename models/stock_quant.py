# -*- coding: utf-8 -*- 

from odoo import models,fields,api,_
from odoo.exceptions import ValidationError


class QuantPackage(models.Model):
    """ Inherit stock package to constraint one product by package """
    _inherit = "stock.quant.package"

    product_id = fields.Many2one('product.product',string='Product',compute='_compute_product',store=True,readonly=False)
    location_id = fields.Many2one(
        'stock.location', 'Location', compute='_compute_package_info',
        index=True, readonly=False, store=True)
