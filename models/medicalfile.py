from odoo import models, fields

class Medicalfile(models.Model):
    _name = "clinc.medicalfile"
    _description = "Medical File "

    numero_dossier = fields.Char(string="Numéro de dossier", required=True)
    observation = fields.Text(string="Observation")

    # Copy fields from prescription
    date = fields.Date(string="Date", default=fields.Date.today)
    doctor_id = fields.Many2one('clinc.doctor', string="Médecin")
    patient_id = fields.Many2one('clinc.patient', string="Patient")
    medicines_ids = fields.One2many(
        'clinc.prescriptionline', 'medicalfile_id', string="Medicaments"
    )
