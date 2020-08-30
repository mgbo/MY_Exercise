
# Inheritance

class Employee:
	raise_amt = 1.04

	def __init__(self, first, last, pay):
		self.first = first
		self.last = last
		self.pay = pay
		self.email = first  + last + '@email.com'

	def fullname(self):
		return '{} {}'.format(str(self.first),str(self.last))

	def apply_raise(self):
		self.pay = int(self.pay * self.raise_amt)

	def __repr__(self):
		return "Employee('{}', '{}', '{}')".format(self.first, self.last, self.pay)


	def __str__(self):
		return '{} --> {} '.format(self.fullname(), self.email)

	def __add__(self, other):
		return self.pay + other.pay

	def __eq__(self, other):
		if self.pay == other.pay:
			return 1

	def __len__(self):
		return len(self.fullname())

	def __mod__(self,other):
		return self.pay%other.raise_amt

	def __contains__(self, item):
		return True if item in self.first else False



emp_1 = Employee('mg', 'kyaw', 400000)
emp_2 = Employee('mg', 'chit', 400000)

#print (emp_1.__repr__())
#print (emp_1.__str__())

#print (repr(emp_1))
#print (str(emp_1))
#print (emp_1)

print (1+2)
print(int.__add__(1,2))
print (str.__add__('myo','chit'))

print (emp_1 + emp_2)
ans = emp_1 + emp_2
print (ans)

print (len('test'))
print ('test'.__len__())

ans_l =len(emp_1)
print (ans_l)

print ('v' in emp_1)

print (emp_1==emp_2)

print (emp_1%emp_2)



