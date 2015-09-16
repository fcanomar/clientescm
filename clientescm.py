# -*- coding: utf-8 -*-

from openerp import models, fields, api

# class clientescm(models.Model):
#     _name = 'clientescm.clientescm'

#     name = fields.Char()

class clientescm_partner (models.Model) :
    _inherit = "res.partner"
    
    x_produccion = fields.Integer(string="Producción")
    
    _sql_constraints = [('nif_unique','UNIQUE(vat)','El NIF introducido corresponde a un cliente ya existente.'),]
    
    @api.multi
    def name_get(self):
        
        res=[]
        
        for item in self:
            
#             if (item.city):
#                 name = item.name + ' (' + item.city + ')'
#             else:
#                 name = item.name
            
            name = item.name + 'TEST'   
                
            res.append((item.id,(name)))
            
        return res
                     
                     
