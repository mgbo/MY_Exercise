
class Employee:
	
	def __init__(self, first, last, pay):
		self.first = first
		self.last = last
		self.pay = pay
		self.email = first + '_' + last + '@gmail.com'

	def fullname(self):
		return '{} {}'.format(self.first,self.last)


emp_1 = Employee('kyaw','thu',5000)
emp_2 = Employee('aung','maung',5999)



print (emp_1.email)
print (emp_2.email)

print (Employee.fullname(emp_1))

print (emp_1.fullname())
ans = emp_2.fullname()
print (ans)