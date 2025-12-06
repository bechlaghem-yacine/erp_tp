from odoo import models, fields, api
from odoo.exceptions import UserError

class ResetMedicinesWizard(models.TransientModel):
    _name = "clinc.reset.medicines.wizard"
    _description = "Reset Medicines Wizard"

    prescription_id = fields.Many2one('clinc.prescription', string="Prescription", required=True)

    def reset_medicines(self):
        """Delete all medicine lines linked to the prescription."""
        self.ensure_one()

        if not self.prescription_id.prescriptionline_ids:
            raise UserError("Cette prescription n'a aucun médicament à supprimer.")

        # Confirm deletion
        if not self.env.context.get('confirm', False):
            return {
                'warning': {
                    'title': "Confirmation",
                    'message': "Vous êtes sur le point de supprimer tous les médicaments de cette prescription !",
                }
            }

        # Delete all lines
        self.prescription_id.prescriptionline_ids.unlink()

        return {'type': 'ir.actions.act_window_close'}
