from odoo import models, fields, api

class AddMedicineWizard(models.TransientModel):
    _name = "clinc.add.medicine.wizard"
    _description = "Wizard to add medicine to existing prescription"

    prescription_id = fields.Many2one(
        'clinc.prescription',
        string="Prescription",
        required=True
    )

    medication_id = fields.Many2one(
        'clinc.medicine',
        string="Medication",
        required=True
    )

    dosage = fields.Char(string="dosage", required=True)
    intake_date = fields.Date(string="Date de prise", required=True)
    instructions = fields.Text(string="Instructions", required=True)


    def add_medicine(self):
        """Add a new prescription line to the existing prescription using append()."""
        self.ensure_one()

        # Create the line using append()
        self.prescription_id.prescriptionline_ids = [
            (0, 0, {
                'medication_id': self.medication_id,
                'dosage': self.dosage,
                'intake_date': self.intake_date,
                'prescription_id': self.prescription_id,
                'instructions': self.instructions,

            })
        ]

        return {'type': 'ir.actions.act_window_close'}
