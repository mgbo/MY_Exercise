n = ["1.3", 7.5, "5", 4, "2.4", 1]

ans = sorted(n,key=float)

print (ans)


class Student:
	def __init__(self, name, grade, age):
		self.name = name
		self.grade = grade
		self.age = age

	def __repr__(self):
		return repr((self.name, self.grade, self.age))


student_objects = [Student('john', 'A', 15),Student('Mg','A',12),Student('Kyaw',"B",16)]
sort_objects = sorted(student_objects, key=lambda stud: stud.age)

print (sort_objects)
print (type(sort_objects))
