from odoo import models, fields, api

class Appointment(models.Model):
    _name = "clinc.appointment"
    _description = "Appointments"

    appointment_date = fields.Datetime(string="Appointment Date", required=True)
    reason = fields.Text(string="Reason for Appointment", required=False)
    status = fields.Selection([
    ('planned', 'Planned'),
    ('confirmed', 'Confirmed'),
    ('cancelled', 'Cancelled'),
    ('completed', 'Completed')
    ], string="Status", default='planned', required=True)
    doctor_id = fields.Many2one('clinc.doctor', string="Doctor", required=True)
    patient_id = fields.Many2one('clinc.patient', string="Patient", required=True)
