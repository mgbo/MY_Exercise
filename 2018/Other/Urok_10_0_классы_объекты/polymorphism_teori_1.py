
class Person:
	name = "Ivan"
	age = 10

	def set(self, name, age):
		self.name = name
		self.age = age


class Student(Person):
	course = 1

	

igor = Student()
igor.set("Igor", 23)
print (igor.course)

vlad = Person()
igor.set("Влад", 19)
print (vlad.name+ " " +str(vlad.age))

ivan = Person()
ivan.set ("Иван", 45)
print (ivan.name + " " + str(ivan.age))