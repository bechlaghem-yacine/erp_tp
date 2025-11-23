from odoo import models, fields, api

class PrescriptionLine(models.Model):
    _name = "clinc.prescriptionline"
    _description = "Medication Line" 
    
    intake_date  = fields.Date(string="Intake Date", required=True)
    dosage  = fields.Char(string="Dosage ", required=True)
    instructions = fields.Text(string="Instructions", required=True)
    medication_id = fields.Many2one('clinc.medicine', string="Medication", required=True)
    prescription_id = fields.Many2one('clinc.prescription', string="Prescription", required=True)
    
    
    @api.onchange('medication_id')
    def _onchange_medication(self):
        if self.medication_id:
            self.dosage = self.medication_id.default_dosage
        else:
            self.dosage = False
