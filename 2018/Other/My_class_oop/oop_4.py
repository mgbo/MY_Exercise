
# Inheritance

class Employee:
	raise_amt = 1.04

	def __init__(self, first, last, pay):
		self.first = first
		self.last = last
		self.pay = pay
		self.email = first  + last + '@email.com'

	def fullname(self):
		return '{} {}'.format(self.first, self.last)

	def apply_raise(self):
		self.pay = int(self.pay * self.raise_amt)

	@classmethod
	def set_raise_amt(cls, amount):
		cls.raise_amt = amount

class Developer(Employee):
	
	raise_amt = 1.10

	def __init__(self, first, last, pay, prog_lang):
		super().__init__(first, last, pay)
		self.prog_lang = prog_lang

class Manager(Employee):
	#raise_amt = 1.12

	def __init__(self, first, last, pay, employee = None):
		super().__init__(first, last, pay)
		if employee is None:
			self.employee = []
		else:
			self.employee = employee

	def add_emp(self, emp):
		if emp not in self.employee:
			self.employee.append(emp)

	def remove_emp(self, emp):
		if emp in self.employee:
			self.employee.remove(emp)

	def print_emps(self):
		for emp in self.employee:
			print ('------>',emp.fullname())
			
			

if __name__ == "__main__":
	dev_1 = Developer('mg', 'kyaw', 500000, 'Python')
	dev_2 = Developer('mg', 'mg', 500000, 'C++')
	dev_3 = Developer('mg', 'aung', 53000, 'Java')

	#print (dev_1.prog_lang)
	#print (dev_1.email)

	mgr_1 = Manager('mg', 'kaung', 90000, [dev_1, dev_2])
	mgr_1.print_emps()
	print ('--------')
	mgr_1.add_emp(dev_1)
	mgr_1.print_emps()
	mgr_1.remove_emp(dev_3)

	print ('--------')
	mgr_1.print_emps()

	print (isinstance(mgr_1, Developer))

	print (isinstance(mgr_1, Employee))






