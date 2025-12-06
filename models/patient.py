# -*- coding: utf-8 -*-
from odoo import models, fields , api
class Patient(models.Model):
    _name = 'clinc.patient'
    _description = "Patient Management"
    _rec_name='firstname'

    firstname=fields.Char(string="firstname",required=True)
    lastname=fields.Char(string="lastname")
    birthday=fields.Date(string="birth date",required=True)
    nationality=fields.Char(string="Nationality",required=True)
    sex=fields.Selection([
        ('male','Male'),
        ('female','Female')
        ],string="sex",required=True)
    image = fields.Binary(string="Photo")





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


    weight_ids = fields.One2many(
        'clinc.patient.weight',
        'patient_id',
        string="Weight Records"
    )

    height_cm = fields.Float(string="Height (cm)")

    bmi = fields.Float(
        string="BMI",
        compute="_compute_bmi",
        store=True
    )

    @api.depends('height_cm', 'weight_ids.weight')
    def _compute_bmi(self):
        for rec in self:
            if rec.height_cm and rec.weight_ids:
                latest_weight = rec.weight_ids[-1].weight  # last weight
                height_m = rec.height_cm / 100
                if height_m > 0:
                    rec.bmi = latest_weight / (height_m ** 2)
                else:
                    rec.bmi = 0
            else:
                rec.bmi = 0

