

class Person:
	num_p = 0
	def __init__(self, name, job=None, pay=0):
		self.name = name
		self.job = job
		self.pay = pay
		Person.num_p +=1

	def lastName(self):
		return self.name.split()[-1]

	def giveRaise(self, percent):
		self.pay = int(self.pay * (1 + percent))

	def __str__(self):
		return "[Person %d: %s, %s, %s]" %(Person.num_p, self.name, self.job, self.pay)

class Manager(Person):
	def __init__(self, name, pay): 
		Person.__init__(self, name, 'mgr', pay)

	def giveRaise(self, percent, bonus=1000):
		Person.giveRaise(self, percent + bonus)

ivan = Person('Иван Petrov')
print (ivan)


john = Person('john Sidorov', job='dev', pay=10000)
print (john)

print (ivan.lastName())

tom = Manager('Tom Jones', 50000)
print (tom)

john.giveRaise(.10)
print (john.pay)

tom.giveRaise(.10)
print (tom.pay)

