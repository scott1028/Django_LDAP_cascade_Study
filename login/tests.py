from django.test import TestCase

# Create your tests here.

from django_auth_ldap.backend import LDAPBackend
ldapobj = LDAPBackend()
user = ldapobj.authenticate('scott.lan','123456')
print user, 1

# import pdb; pdb.set_trace() # by scott
