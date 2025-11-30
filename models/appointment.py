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
    ], string="Status", default='planned',  compute='_compute_appointment_date',
        store=True   )
    doctor_id = fields.Many2one('clinc.doctor', string="Doctor", required=True)
    patient_id = fields.Many2one('clinc.patient', string="Patient", required=True)

    @api.depends('appointment_date')

    def _compute_appointment_date   (self):
        current_date = fields.Datetime.now().date()

        for appointment in self:
            if appointment.appointment_date:
                appointment_date = appointment.appointment_date.date()
                if appointment_date == current_date:
                    appointment.status = 'completed'
                elif appointment_date < current_date:
                    appointment.status = 'planned'
      
