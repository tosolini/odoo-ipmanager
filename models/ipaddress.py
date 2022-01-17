# -*- coding: utf-8 -*-

from odoo import models, fields

class Ipmanager_ipaddress(models.Model):
    _name = 'ipaddress'
    _description = 'IP Address'

    name = fields.Char()

    address_ip = fields.Char(string="IP Address", required=True)
    hostname = fields.Char(string="DNS Name")
    macaddress = fields.Char(string="Mac Address")
    is_dhcp = fields.Boolean(string="DHCP")
    network_id = fields.Many2one('network', string="Subnet")
    wall = fields.Char()
    switch = fields.Char()
    note = fields.Text(string="Note")