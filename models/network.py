# -*- coding: utf-8 -*-

from odoo import models, fields, api
import ipaddress

class Ipmanager_network(models.Model):
    _name = 'network'
    _description = 'Network'

    name = fields.Char()
    network_address = fields.Char(string="Network IP", required=True)
    vlan_id = fields.Many2one('vlan', string="VLAN")

    subnetting = [
        ('8', '/8 - 255.0.0.0 (16777214 hosts)'),
        ('9', '/9 - 255.128.0.0 (8388606 hosts)'),
        ('10', '/10 - 255.192.0.0 (4194302 hosts)'),
        ('11', '/11 - 255.224.0.0 (2097150 hosts)'),
        ('12', '/12 - 255.240.0.0 (1048574 hosts)'),
        ('13', '/13 - 255.248.0.0 (524286 hosts)'),
        ('14', '/14 - 255.252.0.0 (262142 hosts)'),
        ('15', '/15 - 255.254.0.0 (131070 hosts)'),
        ('16', '/16 - 255.255.0.0 (65534 hosts)'),
        ('17', '/17 - 255.255.128.0 (32766 hosts)'),
        ('18', '/18 - 255.255.192.0 (16382 hosts)'),
        ('19', '/19 - 255.255.224.0 (8190 hosts)'),
        ('20', '/20 - 255.255.240.0 (4094 hosts)'),
        ('21', '/21 - 255.255.248.0 (2046 hosts)'),
        ('22', '/22 - 255.255.252.0 (1022 hosts)'),
        ('23', '/23 - 255.255.254.0 (510 hosts)'),
        ('24', '/24 - 255.255.255.0 (254 hosts)'),
        ('25', '/25 - 255.255.255.128 (126 hosts)'),
        ('26', '/26 - 255.255.255.192 (62 hosts)'),
        ('27', '/27 - 255.255.255.224 (30 hosts)'),
        ('28', '/28 - 255.255.255.240 (14 hosts)'),
        ('29', '/29 - 255.255.255.248 (6 hosts)'),
        ('30', '/30 - 255.255.255.252 (2 hosts)'),
    ]

    subnet = fields.Selection(subnetting, string="Subnet", required=True)
    address_ip_ids = fields.One2many('ipaddress', 'network_id', string="IP Address")
    note = fields.Text(string="Note")

    # calculate the number of hosts in the network
    @api.multi
    def create_network(self):
        compose_net = self.network_address + "/" + self.subnet
        calculate_addr = ipaddress.ip_network(compose_net).hosts()
        for addr in calculate_addr:
            self.write({
                    'address_ip_ids': self.write_ipaddress(addr.compressed)
                })

    # write the ipaddress in the database
    @api.multi
    def write_ipaddress(self,arg):
        ispresent = self.env["ipaddress"].search([('address_ip','=',arg)]) 
        if ispresent:
            for x in ispresent:
                if x:
                    x.write({
                        'address_ip': arg,
                        'network_id': self.id,
                    })
        else:
            self.env["ipaddress"].create({
                'address_ip': arg,
                'network_id': self.id,
            })