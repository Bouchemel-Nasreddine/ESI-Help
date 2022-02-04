# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

import string
from setuptools import Require
from odoo import api, fields, models, _


class Demande(models.Model):

    _name = "esi_help.demande"
    _description = "desc"

    etat_validation = False

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
    #etat_validation = fields.Boolean(_etat_validation)
    def action_valider (self):
        #self.etat_validation=True
        print('mmmm')
    def action_creer_projet (self):
        if self.etat_validation :
            print('mmm')
        