
import sys
print (sys.executable)
print (sys.version)

print ('-------------')

class Emploee:
	""" A sample Emploee class """

	def __init__(self, first, last):
		self.first = first
		self.last = last 

	@property
	def email(self):
		return '{}{}@gmail.com'.format(self.first,self.last)

	@property
	def fullname(self):
		return '{} {}'.format(self.first, self.last)

for n in [1,2,3,4,5]:
	print (n)

emp1 = Emploee('Thein', 'Hla')

emp1.my = 'chit'
print(emp1.my)

print (emp1.first)
print (emp1.email)
print (emp1.fullname)










