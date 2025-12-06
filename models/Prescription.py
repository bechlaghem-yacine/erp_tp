from odoo import models, fields, api

class Prescription(models.Model):
    _name = "clinc.prescription"
    _description = "Medical Prescriptions"

    date = fields.Date(string="Date", required=True, default=fields.Date.context_today,
    readonly=True,)
    prescriptionline_ids = fields.One2many('clinc.prescriptionline', 'prescription_id', string="medicines")
    doctor_id = fields.Many2one('clinc.doctor', string="Doctor", required=True) 
    patient_id = fields.Many2one('clinc.patient', string="Patient", required=True)