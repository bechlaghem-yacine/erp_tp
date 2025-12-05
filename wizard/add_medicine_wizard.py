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

    posologie = fields.Char(string="Posologie", required=True)
    date_prise = fields.Date(string="Date de prise", required=True)

    def add_medicine(self):
        """Add a new prescription line to the existing prescription using append()."""
        self.ensure_one()

        # Create the line using append()
        self.prescription_id.medicines_ids = [
            (0, 0, {
                'medication_id': self.medication_id.id,
                'dosage': self.posologie,
                'intake_date': self.date_prise,
                'prescription_id': self.prescription_id.id,
            })
        ]

        return {'type': 'ir.actions.act_window_close'}
