"""
We have entries in a database of users which are represented in Python as a dictionary of key-value pairs,
where each key is a case-insensitive string object and each value is a list of bytes objects.

For example:

  db_dict = {
      'objectclass': [b'inetOrgPerson', b'person'],
      'cn': [b'Peter Sellers'],
      'givenName': [b'Peter'],
      'sn': [b'Sellers'],
      'uidNumber': [b'1925'],
      'gidNumber': [b'1925'],
      'mail': [
      b'peter.sellers@example.com',
      b'fu.manchu@example.com',
  ],
  }

Create an DbEntry class with attributes for each of the keys listed above that can be used as follows:

  entry = DbEntry(db_dict)
  assert(entry.cn == 'Peter Sellers')
  assert(entry.uidNumber == 1925)
  assert('peter.sellers@example.com' in entry.mail)
  assert(len(entry.mail) == 2)

"""


class DbEntry:
    """
    This is a class for DB Entries
    """

    def __init__(self, ldap_object):
        # allocate dictionary of keys for case-insentitivity
        definition_dict = {
            'objectclass': ('objectclass', self.to_list),
            'cn': ('cn', self.get_first_string),
            'givenname': ('givenName', self.get_first_string),
            'sn': ('sn', self.get_first_string),
            'uidnumber': ('uidNumber', self.to_integer),
            'gidnumber': ('gidNumber', self.to_integer),
            'mail': ('mail', self.to_list),
        }

        for key, val in ldap_object.items():
            key = key.lower()
            setattr(self, definition_dict[key][0], definition_dict[key][1](val))

        # Ensure all attributes are allocated
        for key, val in definition_dict.items():
            if val[0] not in self.__dict__:
                setattr(self, val[0], None)

    @staticmethod
    def to_list(val):
        return [k.decode("utf-8") for k in val]

    @staticmethod
    def get_first_string(val):
        # It is not clear If the first value is the expected or a different behaviour
        return val[0].decode("utf-8")

    @staticmethod
    def to_integer(val):
        return int(val[0])
