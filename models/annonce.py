# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from setuptools import Require
from odoo import api, fields, models, _

class Annonce(models.Model):

    _name = "esi_help.annonce"
    _description = "desc"

    #projet = fields.many2one('esi_help.projet', 'projet associé', Required=True)