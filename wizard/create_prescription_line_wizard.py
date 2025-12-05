from odoo import models, fields

class CreatePrescriptionLineWizard(models.TransientModel):
    _name = "clinc.create.prescription.line.wizard"
    _description = "Wizard Medicine Line"

    wizard_id = fields.Many2one("clinc.create.prescription.wizard")
    medication_id = fields.Many2one(
        'clinc.medicine',
        string="Medication",
        required=True
    )
    posologie = fields.Char(string="Posologie", required=True)
    date_prise = fields.Date(
        string="Date de prise",
        default=fields.Date.context_today
    )
