import ldap
import ldap3
import logging
import sys
from pprint import pprint

logger = logging.getLogger('example_logger')

LDAP_SERVER = "ldap://192.168.99.119"
LDAP_BASE = "dc=nomad,dc=local"
attrs = ['cn']

def users_ldap_groups(uid):
    server = ldap3.Server(LDAP_SERVER)
    #search_filter=
    search_filter='(member:1.2.840.113556.1.4.1941:=CN=muffin man,OU=Raleigh,DC=nomad,DC=local)'
    with ldap3.Connection(server,'CN=bob villa,OU=Raleigh,DC=nomad,DC=local','Password1', auto_bind=True) as conn:
        conn.search(LDAP_BASE, search_filter, attributes=attrs)
        pprint(conn.entries)
    
    
    # try:
    #     # this returns the groups!
    #     results = l.search_s(LDAP_BASE, ldap.SCOPE_SUBTREE, search_filter, ['cn'])
    #     ldap_groups = []
    #     #logger.debug('%s groups: %s' % (uid, results) )
    #     for i in results:
    #         pprint(i[1])
    #         thing = i
    #     return thing 
    # except ldap.NO_SUCH_OBJECT as e:
    #     logger.error("{}:{}unable to lookup uid {} on LDAP server {}: {}".format(__file__, sys._getframe().f_code.co_name, uid, LDAP_SERVER, e))
    #     return False
    # #except Exception as e: # some other error occured
    #  #   logger.error("{}:{}: other error occurred looking up {} in LDAP: {}".format(__file__, sys._getframe().f_code.co_name,uid,e))
    #   #  return False
    # # shouldn't get here, but if we do, we don't have any results!
    # return False

pprint(users_ldap_groups('muffin.man'))