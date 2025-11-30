# -*- coding: utf-8 -*-
from odoo import models, fields , api
class Patient(models.Model):
    _name = 'clinc.patient'
    # _description = "Patient Management"
    # _rec_name='firstname'

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
    # weight_history_ids = fields.One2many(
    #     'clinc.patient.weight',
    #     'patient_id',
    #     string="Historique des poids"
    # )

    nbr_prescription = fields.Integer(
        string="Nombre de prescriptions",
        compute='_compute_nbr_prescription',
        store=True   
    )

    @api.depends('prescription_ids')
    def _compute_nbr_prescription(self):
        for patient in self:
            patient.nbr_prescription = len(patient.prescription_ids)



# class PatientWeight(models.Model):
#     _name = "clinc.patient.weight"
#     _description = "Patient Weight History"

#     patient_id = fields.Many2one(
#         'clinc.patient',
#         string="Patient",
#         required=True,
#         ondelete="cascade"
#     )

#     weight = fields.Float(string="Poids (kg)", required=True)
#     date = fields.Date(string="Date", default=fields.Date.today)
