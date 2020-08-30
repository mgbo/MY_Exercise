
class Employee:
	num_of_emp = 0
	raise_amount = 1.04

	def __init__(self, first, last, pay):
		self.first = first
		self.last = last
		self.email = first + '.' + last +'@gmail.com'
		self.pay = pay
		#self.num_of_emp +=1
		Employee.num_of_emp +=1

	def fullname(self):
		return '{} {}'.format(self.first, self.last)

	def apply_raise(self):
		self.pay = int(self.pay *  self.raise_amount)

emp_1 = Employee('Corey', 'Schafer', 50000)
emp_2 = Employee('Test', 'Employee', 60000)

print ("Number of Employee : {}".format(Employee.num_of_emp))

print (emp_1.fullname())
print (emp_1.raise_amount)


print (emp_1.pay)
emp_1.apply_raise()
print (emp_1.pay)













