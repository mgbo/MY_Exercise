
class Person(object):
	def __init__(self, name, job=None, pay=0, part_time=1):
		self.name = name
		self.job = job
		self.base_pay = pay
		self.part_time = part_time

	def __repr__(self):
		return '{} {} {} '.format(self.name, self.job, self.base_pay)

	def get_familiya(self):
		return self.name.split()[2]

	def pay(self):
		return self.base_pay * self.part_time

class Teacher(Person):
	HOUR_PAY = 100

	def __init__(self, name, pay=0, part_time=0, hour=0):
		super().__init__(name, job='Teacher', pay=pay, part_time=part_time)
		self.hour = hour
		self.courses = set()

	def pay(self):
		res = super().pay() + self.hour * Teacher.HOUR_PAY

	def add_course(self, course):
		self.courses.add(course)

	def revove_course(self, course):
		self.courses.remove(course)

	def get_course(self):
		return self.get_familiya() + ' : ' + ' '.join(self.courses)

	def upgrade(self):
		self.job = 'Senior Teacher'



bob = Person('Boris Alexeevich Ivanov')
mike = Person('Mikhail Valdimirovich Kuznetsov', job='student', pay=50000)

tanya = Teacher('Tatyana Vladimirovna Ovayannikova', pay=10000, hour=6*4)

print(mike)
print (tanya)

tanya.add_course('Informatica')
tanya.add_course('IPC')

tanya.upgrade()
print (tanya.get_course())
print(tanya)













