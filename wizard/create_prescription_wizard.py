from odoo import models, fields, api

class CreatePrescriptionWizard(models.TransientModel):
    _name = "clinc.create.prescription.wizard"
    _description = "Wizard to Create Prescription"

    patient_id = fields.Many2one("clinc.patient", string="Patient", readonly=True)
    doctor_id = fields.Many2one("clinc.doctor", string="Médecin", required=True)

    medicine_line_ids = fields.One2many(
        "clinc.create.prescription.line.wizard",
        "wizard_id",
        string="Médicaments"
    )

    def create_prescription(self):
        """Create prescription + prescription lines"""
        prescription = self.env['clinc.prescription'].create({
            'patient_id': self.patient_id.id,
            'doctor_id': self.doctor_id.id,
            'date': fields.Date.context_today(self),
        })

        for line in self.medicine_line_ids:
            self.env['clinc.prescriptionline'].create({
                'prescription_id': prescription.id,
                'medicine': line.medicine,
                'posologie': line.posologie,
                'date_prise': line.date_prise
            })

        return {'type': 'ir.actions.act_window_close'}
