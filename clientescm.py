# -*- coding: utf-8 -*-

from openerp import models, fields, api

# class clientescm(models.Model):
#     _name = 'clientescm.clientescm'

#     name = fields.Char()

class clientescm_partner (models.Model) :
    _inherit = "res.partner"
    
    display_name = fields.Char(string="Name", compute='_compute_display_name')
    x_produccion = fields.Integer(string="Producción")

    
    _sql_constraints = [('nif_unique','UNIQUE(vat)','El NIF introducido corresponde a un cliente ya existente.'),]
    
#     @api.one
#     @api.depends('name','parent_id.name')
#     def _compute_display_name(self):
# 
#         self.display_name = self.name + " (" + self.city + ")" 
        
class clientescm_crmlead(models.Model):
    _inherit = "crm.lead"
    
    x_poblacion = fields.Char(related='partner_id.city', string='Población')
           
