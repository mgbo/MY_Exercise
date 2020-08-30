
class Employee():
	def __init__(self, name, age, salary):
		self.name = name
		self.age = age
		self.salary = salary

	def __repr__(self):
		return 'Name :{}, Age :{}, Salary : {} $'.format(self.name, self.age, self.salary)

if __name__ == "__main__":
	e1 = Employee('aung kayw', 37, 60000)
	e2 = Employee('aaaw gyi', 35, 60000)
	e3 = Employee('htet ko', 34, 1000)

	print (e1)
	employees = [e1, e2, e3]

	def e_sort(emp):
		return emp.salary, emp.name


	#print (employees)

	s_employees = sorted(employees, key=e_sort)
	print (s_employees)


	for worker in s_employees:
		print (worker)






