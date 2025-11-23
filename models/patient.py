# -*- coding: utf-8 -*-
from odoo import models, fields , api
class Patient(models.Model):
    _name = 'clinc.patient'
    _description = "Patient Management"
    _rec_name='Firstname'

    firstname=fields.Char(string="firstname",required=True)
    lastname=fields.Char(string="lastname",required=True)
    birthday=fields.Date(string="birth date",required=True)
    nationality=fields.Char(string="Nationality",required=True)
    sex=fields.Selection([
        ('male','Male'),
        ('female','Female')
        ],string="sex",required=True)
    appointment_ids = fields.One2many('clinc.appointment', 'patient_id', string="appointments")
    prescription_ids = fields.One2many('clinc.prescription', 'patient_id', string="Prescriptions")

    nbr_prescription = fields.Integer(
        string="Nombre de prescriptions",
        compute='_compute_nbr_prescription',
        store=True   
    )

    @api.depends('prescription_ids')
    def _compute_nbr_prescription(self):
        for patient in self:
            patient.nbr_prescription = len(patient.prescription_ids)



