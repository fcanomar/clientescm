# -*- coding: utf-8 -*-

from openerp import models, fields, api

# class clientescm(models.Model):
#     _name = 'clientescm.clientescm'

#     name = fields.Char()

class clientescm_partner (models.Model) :
    _inherit = "res.partner"
    
    x_produccion = fields.Integer(string="Producción")
    
    _sql_constraints = [('nif_unique','UNIQUE(vat)','El NIF introducido corresponde a un cliente ya existente.'),]
                     
                     
