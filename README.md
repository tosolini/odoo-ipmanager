# odoo-ipmanager
IP Management ad Odoo APP

This app is made for take note about Networks and corresponding IP Addresse's, hostname's and where those are attached.

App is compose by three part, Network, Ip Address and Vlan.

# VLAN
Vlan can include one or multiple network. This part is also available on the Network Form.

# Network
Network request a Full IP Address (e.g. 192.168.1.0) and the Subnet Mask (e.g. /24) and obviously a name for recognized them.

After the field IP Address and Subnet are provided, you can press "Generate IP" and the corrisponded host's available to this network are created or updated. The subnet effect the number of IP's to the tree list.

# IP Address
This is the whole list of IP Address recorded to the database. Every one refer to their network. The main form offer some clue's like the wall port or Switch Port. You can record the hostname in the Local DNS, the MAC Address and a small note.