# -*- coding: utf-8 -*-
from odoo import models, fields
class Patient(models.Model):
    _name = 'clinc.patient'
    _description = "Patient Management"

    firstname=fields.Char(string="firstname",required=True)
    lastname=fields.Char(string="lastname",required=True)
    birthday=fields.Date(string="birth date",required=True)
    Nationality=fields.Char(string="Nationality",required=True)
    sex=fields.Selection([
        ('male','Male'),
        ('female','Female')
        ],string="sex",required=True)
    appointment_ids = fields.One2many('clinc.appointment', 'patient_id', string="appointments")
    prescription_ids = fields.One2many('clinc.prescription', 'patient_id', string="Prescriptions")



