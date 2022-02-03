# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from setuptools import Require
from odoo import api, fields, models, _


class Demande(models.Model):

    _name = "esi_help.demande"
    _description = "desc"

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