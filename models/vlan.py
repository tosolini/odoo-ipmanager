# -*- coding: utf-8 -*-

from odoo import models, fields

class Ipmanager_vlan(models.Model):
    _name = 'vlan'
    _description = 'VLAN'

    name = fields.Integer()
    description = fields.Char()
    network_id = fields.One2many(comodel_name='network', inverse_name='vlan_id', string="Subnet")