
class Dog:
	kind = 'canine'
	tricks = []

	def __init__(self, name):
		self.name = name

	def add_trick(self, trick):
		self.tricks.append(trick)

d = Dog('Fibo')
e = Dog('Buddy')

print (e.kind)
print (e.name)
print (d.name)

d.add_trick('rool over')
e.add_trick('play')

print (d.tricks)
print (e.tricks)
