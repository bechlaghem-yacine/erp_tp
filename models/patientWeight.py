from odoo import models, fields

class PatientWeight(models.Model):
    _name = 'clinc.patient.weight'
    _description = "Patient Weight Records"

    weight = fields.Float(string="Weight (kg)", required=True)
    date = fields.Date(string="Date", default=fields.Date.today)
    patient_id = fields.Many2one('clinc.patient', string="Patient")
