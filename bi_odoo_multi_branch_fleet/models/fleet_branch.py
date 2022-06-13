# -*- coding: utf-8 -*-
# Part of BrowseInfo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models, _
from odoo.exceptions import UserError

class ResBranch(models.Model):
    _name = 'res.branch'
    
    name = fields.Char('Name', required=True)
    address = fields.Text('Address', size=252)
    telephone_no = fields.Char("Telephone No")
    company_id =  fields.Many2one('res.company', 'Company', required=True)


class ResUsers(models.Model):
    _inherit = 'res.users'
    
    branch_id = fields.Many2one('res.branch', 'Branch')
    branch_ids = fields.Many2many('res.branch',string='Allowed Branches')
    
class FleetVehicle(models.Model):
    _inherit = 'fleet.vehicle'

    branch_id = fields.Many2one('res.branch', string='Branch') 
    
    @api.model 
    def default_get(self, flds): 
        result = super(FleetVehicle, self).default_get(flds)
        user_obj = self.env['res.users']
        branch_id = user_obj.browse(self.env.user.id).branch_id.id
        result['branch_id'] = branch_id
        return result
    
class VehicleOdometer(models.Model):
    _inherit = 'fleet.vehicle.odometer'

    branch_id = fields.Many2one('res.branch', string='Branch') 
    
    @api.onchange('vehicle_id')
    def _onchange_vehicle_id(self):
        if self.vehicle_id:
            self.branch_id = self.vehicle_id.branch_id

class FleetVehicleLogContract(models.Model):
    _inherit = 'fleet.vehicle.log.contract'

    branch_id = fields.Many2one('res.branch', string='Branch') 
    
    @api.onchange('vehicle_id')
    def _onchange_vehicle_id(self):
        if self.vehicle_id:
            self.branch_id = self.vehicle_id.branch_id

class FleetVehicleLogServices(models.Model):
    _inherit = 'fleet.vehicle.log.services'

    branch_id = fields.Many2one('res.branch', string='Branch')  
    
    @api.onchange('vehicle_id')
    def _onchange_vehicle_id(self):
        if self.vehicle_id:
            self.branch_id = self.vehicle_id.branch_id
           
# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
