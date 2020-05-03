
from device_info import ios_xe1
from ncclient import manager
import xmltodict
import xml.dom.minidom
from pprint import pprint

# NETCONF filter to use
config_template = open("config-temp-ietf-interfaces.xml").read()

if __name__ == '__main__':

    netconf_config = config_template.format(int_name="GigabitEthernet2",
                                            int_desc="Configured by TERENCE",
                                            ip_address="10.255.255.2",
                                            subnet_mask="255.255.255.0")

    print("Configuration Payload:")
    print("----------------------")
    print(netconf_config)

if __name__ == '__main__':
    with manager.connect(host=ios_xe1["address"], port=ios_xe1["port"],
                         username=ios_xe1["username"],
                         password=ios_xe1["password"],
                         hostkey_verify=False) as m:

        device_reply = m.edit_config(netconf_config, target="running")
        print(device_reply)
