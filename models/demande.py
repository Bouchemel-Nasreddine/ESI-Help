# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

import string
from setuptools import Require
from odoo import api, fields, models, _


class Demande(models.Model):

    _name = "esi_help.demande"
    _description = "desc"

    etat_validation = fields.Boolean(String='status')
    user_id = fields.Many2one('res.users', String='demandeur', required=True)
    name = fields.Char(string='titre',  required=True)
    contenu = fields.Text(string='contenu', required=True)
    nature = fields.Selection(
        [
            ('finance', 'demande financiere'),
            ('assiste', 'assistance sur un projet'),
            ('trajet', 'trajet à faire'),
            ('médic', 'demande de médicament'),
        ], 
        required=True)
        
    #la fonction de validation du demande, le boutton valider va se disparaitre, et le boutton creer projet va s'affihcer
    def action_valider (self):
        self.etat_validation=True

    #la foncion du creation du projet automatiquement
    def action_creer_projet(self):
        name = _('Créer projet')
        return {
            'name': name,
            'view_type': 'form',
            'view_mode': 'form',
            'res_model': 'esi_help.projet',
            'type': 'ir.actions.act_window',
            'target': 'current',
}
        