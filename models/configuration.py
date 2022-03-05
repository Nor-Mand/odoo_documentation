# -*- coding: utf-8 -*-
from odoo import fields, models

class Configutarion(models.Model):
    _name = 'config'

    name = fields.Char(string='Name')