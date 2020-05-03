#! /usr/bin/env python
"""
Learning Series: Network Programmability Basics
Module: Network Device APIs
Lesson: Goodbye SNMP hello NETCONF
Author: Hank Preston <hapresto@cisco.com>

example2.py
Illustrate the following concepts:
- Send <get> to retrieve config and state data
- Process and leverage XML within Python
- Report back current state of interface
"""

__author__ = "Hank Preston"
__author_email__ = "hapresto@cisco.com"
__copyright__ = "Copyright (c) 2016 Cisco Systems, Inc."
__license__ = "MIT"

from device_info import ios_xe1
from ncclient import manager
import xmltodict
import xml.dom.minidom
from pprint import pprint

# NETCONF filter to use
netconf_filter = open("filter-ietf-interfaces.xml").read()

if __name__ == '__main__':
    with manager.connect(host=ios_xe1["address"], port=ios_xe1["port"],
                         username=ios_xe1["username"],
                         password=ios_xe1["password"],
                         hostkey_verify=False) as m:

        # Get Configuration and State Info for Interface
        interface_netconf = m.get(netconf_filter)

        # Process the XML and store in useful dictionaries
        """
        xmlDom = xml.dom.minidom.parseString(str(interface_netconf))
        print(xmlDom.toprettyxml(indent=" "))
        print('*' * 25 + 'Break' + '*' * 50)
        """

        # Converting xml to python option

        interface_python = xmltodict.parse(interface_netconf.xml)[
            "rpc-reply"]["data"]
        pprint(interface_python)
        name = interface_python['interfaces']['interface']['name']['#text']
        print(name)

        config = interface_python["interfaces"]["interface"]
        op_state = interface_python["interfaces-state"]["interface"]

        print("Start")
        print(f"Name: {config['name']['#text']}")
        print(f"Description: {config['description']}")
        print(f"Packets In {op_state['statistics']['in-unicast-pkts']}")
