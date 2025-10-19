from odoo import models, fields, api

class PrescriptionLine(models.Model):
    _name = "clinc.prescriptionline"
    _description = "Medication Line" 
    intake_date  = fields.Date(string="Intake Date", required=True)
    dosage  = fields.Char(string="Dosage ", required=True)
    medication_id = fields.Many2one('clinc.Medicine', string="Medication", required=True)
    prescription_id = fields.Many2one('clinc.prescription', string="Prescription", required=True)