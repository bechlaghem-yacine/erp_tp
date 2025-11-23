from odoo import models, fields, api

class Medicine(models.Model):
    _name = "clinc.medicine"
    _description = "Medicines Management"
    _rec_name='commercial_name'

    commercial_name = fields.Char(string="Commercial Name", required=True)
    dci = fields.Char(string="DCI", required=True)
    form = fields.Selection([
    ('capsule', 'Capsule'),
    ('syrup', 'Syrup'),
    ('tablet', 'Tablet'),
    ('ointment', 'Ointment'),
    ('gel', 'Gel'),
    ('injection', 'Injection')
    ], string="Form", required=True)
    prescription_line_ids = fields.One2many('clinc.prescriptionline', 'medication_id', string="prescription lines")

    default_dosage = fields.Char(string="Dosage par défaut", 
                                 help="Ex: 500 mg, 1 comprimé")
