# -*- coding: utf-8 -*-
from odoo import fields, models

class AbstractModel(models.Model):
    _name = 'doc.abstract'

    name = fields.Char(string='Name')