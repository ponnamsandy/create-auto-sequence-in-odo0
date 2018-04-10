# -*- coding: utf-8 -*-

from odoo import models, fields, api,_

class emp_statusbar(models.Model):
    _name = 'emp_statusbar.emp_statusbar'

    name = fields.Char()
    value = fields.Integer()

class Employee(models.Model):
    _inherit = "hr.employee"

    employee_id = fields.Char(string="Employee-Id",readonly="True")
    #default create auto sequence ids 
    #default=lambda self: self.env['ir.sequence'].next_by_code('hr.employee')
    state = fields.Selection([
            ('probation', 'Probation'),
            ('employee', 'Employee'),
            ('resign', 'Resign'),
            ],default='probation')

    @api.one
    def generate_sequence(self):
            
        if self.employee_id == 0:
            next_seq = self.env['ir.sequence'].next_by_code('hr.employee')
            self.employee_id = next_seq
        else:
            pass                                                 

    #generate auto sequence ids when click save button 
    # @api.model
    # def create(self, vals):
    #     vals['employee_id'] = self.env['ir.sequence'].next_by_code('hr.employee')
    #     return super(Employee, self).create(vals)






        
        



        

