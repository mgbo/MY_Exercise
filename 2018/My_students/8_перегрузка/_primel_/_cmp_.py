
class Person(object):
    def __init__(self, firstname, lastname):
        self.first = firstname
        self.last = lastname

    def __cmp__(self, other):
        return cmp((self.last, self.first),(other.last, other.first))

    def __repr__(self):
        return '{} {}'.format(self.first, self.last)

actor = [Person('Eric','Idle'),
         Person('John','Cleese'),
         Person('Michael','Palin'),
         Person('Terry','Gilliam'),
         Person('Terry','Jones')
         ]

for p in actor:
    print (repr(p))

def cmp_last_name(a,b):
    """ compare names by last name"""
    return cmp(a.last, b.last)

#sorted(actor, cmp= cmp_last_name)

for p in actor:
    print (repr(p))
