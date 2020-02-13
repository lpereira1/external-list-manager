from iptools.ipv4 import validate_cidr, validate_ip
import ipaddress


def test_ip(address):
    if '/' in address:
        try:
            ipaddress.ip_network(address)
        except:
             print('It looks like you are trying to put in a host with a network mask.')
    else:
        try:
             ipaddress.ip_address(address)
            
        except:
            print('Invalid CIDR address, please enter a valide CIDR network or host IP')

address_1 = input('Please enter an IP address: \n\r')

test_ip(address_1)

