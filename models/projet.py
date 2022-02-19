# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from setuptools import Require
from odoo import api, fields, models, _

class Demande(models.Model):

    _name = "esi_help.projet"
    _description = "desc"

    name = fields.Char(string='code',  required=True)
    description = fields.Text(string='description', required=True)
    coordonnees = fields.Char(string='coordonnees')
    date_limit = fields.Date(string="date limite")