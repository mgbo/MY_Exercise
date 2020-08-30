
print ('{1} {0}'.format('one', 'two'))

class Data(object):

	def __str__(self):
		return 'str'

	def __repr__(self):
		return 'repr'

print ('%s %r'%(Data(), Data())) #old
print ('{0!s} {0!r}'.format(Data()))
