
class Employee:
	def __init__(self, name, salary=0):
		self.name = name
		self.salary = salary

	def giveRaise(self, percent):
		self.salary = self.salary + (self.salary * percent)

	def work(self):
		print (self.name, "does stuff")

	def __str__(self):
		return "<Employee : name = %s, salary = %s >"%(self.name, self.salary)


class Chef(Employee):
	def __init__(self, name):
		Employee.__init__(self, name, 500000)

	def work(self):
		print(self.name, "makes food")

class Server(Employee):
	def __init__(self, name):
		Employee.__init__(self, name, 40000)

	def work(self):
		print (self.name ,"interfaces with customer")

if __name__ == "__main__":

	bob = Server('bob')
	bob.work()
	bob.giveRaise(0.20)
	print (bob)
	print ("-----------")


	for klass in Employee, Chef,Server:
		obj = klass(klass.__name__)
		obj.work()





















