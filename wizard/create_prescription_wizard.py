from odoo import models, fields, api

class CreatePrescriptionWizard(models.TransientModel):
    _name = "clinc.create.prescription.wizard"
    _description = "Wizard to Create Prescription"

    patient_id = fields.Many2one("clinc.patient", string="Patient", readonly=True)
    doctor_id = fields.Many2one("clinc.doctor", string="Médecin", required=True)

    prescriptionline_ids  = fields.One2many(
        "clinc.create.prescription.line.wizard",
        "wizard_id",
        string="Lignes"
    )

    def create_prescription(self):
        prescription = self.env['clinc.prescription'].create({
            'patient_id': self.patient_id.id,
            'doctor_id': self.doctor_id.id,
            'date': fields.Date.context_today(self),
        })

        created_ids = []
        for line in self.prescriptionline_ids:
            rec = self.env["clinc.prescriptionline"].create({
                "prescription_id": prescription.id,
                "medication_id": line.medication_id.id,
                "dosage": line.dosage,
                "intake_date": line.intake_date,
                "instructions": line.instructions,
            })
            created_ids.append(rec.id)

        # 3) Write One2many with command 6
        prescription.write({
            "prescriptionline_ids": [(6, 0, created_ids)]
        })
        return {'type': 'ir.actions.act_window_close'}
