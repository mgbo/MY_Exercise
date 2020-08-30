

class Employee:

	num_of_emps = 0
	raise_amt = 1.04

	def __init__(self, first, last, pay):
		self.first = first
		self.last = last
		self.email = first + last + '@gmail.com'
		self.pay = pay

		Employee.num_of_emps+=1
		print ('---')

	def fullname(self):
		return '{} {}'.format(self.first, self.last)

	def apply_arise(self):
		self.pay = int(self.pay * self.raise_amt)

	@classmethod
	def set_raise_amt(cls, amount):
		cls.raise_amt = amount

if __name__ == "__main__":

	emp_1 = Employee('mg','kyaw', 500000)
	emp_1 = Employee('mg', 'chit', 6000000)

	print(Employee.raise_amt)
	emp_1.set_raise_amt(8)
	print (emp_1.raise_amt)
































