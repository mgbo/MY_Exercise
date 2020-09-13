
class Employee:

	def __init__(self, first, last, pay):
		self.first = first
		self.last = last
		self.pay = pay

	@property
	def email(self):
		return '{}.{}@gmail.com'.format(self.first, self.last)

	@property
	def fullname(self):
		return '{} {}'.format(self.first, self.last)

	def __repr__(self):
		return 'Employee ({}, {}, {})'.format(self.first, self.last, self.pay)


# e1 = Employee('mg', 'mg', 500)
# print (e1)
# print(e1.fullname)
# e1.first = 'ko'
# print(e1.fullname)
# print (e1)
# print (e1.first)




