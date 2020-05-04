from device_info import ios_xe1
from ncclient import manager
import xmltodict
import xml.dom.minidom
from pprint import pprint


router = {"host": "10.10.20.181", "port": "22", "username": "cisco",
          "password": "cisco"}

# NETCONF filter to use
netconf_filter = open("filter-ietf-interfaces.xml").read()


with manager.connect(host=router["host"], port=router["port"], username=router["username"], password=router["password"], hostkey_verify=False) as m:
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
