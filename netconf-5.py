
from device_info import ios_xe1
from ncclient import manager
import xmltodict
import xml.dom.minidom
from pprint import pprint

router = {"host": "10.10.20.181", "port": "830", "username": "cisco",
          "password": "cisco"}

# NETCONF filter to use
config_template = open("config-temp-ietf-interfaces.xml").read()

if __name__ == '__main__':

    netconf_config = config_template.format(int_name="GigabitEthernet2",
                                            int_desc="Configured by TERENCE",
                                            ip_address="172.31.252.1",
                                            subnet_mask="255.255.255.0")

    print("Configuration Payload:")
    print("----------------------")
    print(netconf_config)

with manager.connect(host=router["host"], port=router["port"], username=router["username"], password=router["password"], hostkey_verify=False) as m:
    device_reply = m.edit_config(netconf_config, target="running")
    print(device_reply)
