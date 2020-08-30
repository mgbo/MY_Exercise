
print ("%s %f %s"%(7,3.17,"hello"))


class Data(object):

    def __str__(self):
        return 'str'

    def __repr__(self):
        return 'repr'

print ('%s %r' %(Data(), Data()))
print ('{0!s} {0!r}'.format(Data()))


# ---------- right alignment -----------
print ('%10s' % ('test',)) # old
print ('{:->10}'.format('test')) # new

# ---------- left alignment -----------
print ('{:-<10}'.format('test')) # new

# ---------- left alignment -----------
print('{:-^10}'.format('test'))
print('{:^10}'.format('test'))


# ----------- Named placeholders ---------------

data = {'first': 'Hodor', 'last': 'Hodor!', 'third':'Hello'}
print ('{first} {last} {third}'.format(**data))











