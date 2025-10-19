from odoo import models, fields
class Doctor(models.Model):
    _name = 'clinc.doctor'
    _description = "Doctors Management"

    firstname=fields.Char(string="firstname",required=True)
    lastname=fields.Char(string="lastname",required=True)
    birthday=fields.Date(string="birth date",required=True)
    Nationality=fields.Char(string="Nationality",required=True)
    specialite = fields.Selection([
        ('cardiologue', 'Cardiologue'),
        ('ophthalmologist', 'Ophthalmologist'),
        ('neurologist', 'Neurologist'),
        ('general', 'General')
    ], string="Spécialité", required=True)
    phone_number = fields.Char(string="Phone number",required=True)
    prescription_ids = fields.One2many('clinc.prescription', 'doctor_id', string="Prescriptions")
    appointment_ids = fields.One2many('clinc.appointment', 'doctor_id', string="appointments")
