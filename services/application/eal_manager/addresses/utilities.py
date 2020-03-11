from eal_manager import db


def generateExport():
    address_list = {}
     for i in IPAddress.query.all():
         address_list.append(i.address)
    return test
