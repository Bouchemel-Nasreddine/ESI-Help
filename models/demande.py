# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from setuptools import Require
from odoo import api, fields, models, _


class Demande(models.Model):

    _name = "esi_help.demande"
    _description = "desc"

    name = fields.Char(string='titre',  required=True)
    Date = fields.Date()
    Archive = fields.Boolean(default =False)
    contenu = fields.Char(string='contenu', required=True)
    nature = fields.Char(string='nature', Required=True)