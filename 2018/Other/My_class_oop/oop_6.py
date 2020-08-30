
class Employee:
	raise_amt = 1.04

	def __init__(self, first, last):
		self.first = first
		self.last = last

	@property
	def email(self):
		return '{}{}@gmail.com'.format(str(self.first),str(self.last))

	@property
	def fullname(self):
		return '{} {}'.format(str(self.first),str(self.last))

	@fullname.setter
	def fullname(self, name):
		first, last = name.split(' ')
		self.first = first
		self.last = last

	@fullname.deleter
	def fullname(self):
		print ('Delete Name!')
		self.first = None
		self.last = None


if __name__ == "__main__":

	emp_1 = Employee('mg', 'kyaw')

	print (emp_1.fullname)


	emp_1.first = 'kyaw'
	emp_1.fullname = 'mg chit'

	print (emp_1.first)
	print (emp_1.email)
	print (emp_1.fullname)

	del emp_1.fullname

	print (emp_1.fullname)





