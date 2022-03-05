# -*- coding: utf-8 -*-
from odoo import fields,models

class Main(models.Model):
    _name = 'main.form'

    name = fields.Char(string='Name')
    last_name = fields.Char(string='Last Name')