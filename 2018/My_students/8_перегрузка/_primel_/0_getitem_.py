

#######################################################

class Person:
	def __init__(self, name, age):
		self.name = name
		self.age = age

	def __getitem__(self, key):
		print ("Inside __getitem__ method!!")
		return getattr(self, key) # выполняет индексирование


p = Person('chit', 23)
print (p["age"])

print ("============================")


#######################################################

class Buliding(object):
	def __init__(self, floors):
		self._floors = [None]*floors

	def occupy(self, floors_number, data):
		self._floors[floors_number] = data

	def get_floor_data(self, floors_number):
		return self._floors[floors_number]

	def __repr__(self):
		s=''.join([str(s) for s in self._floors])
		return s

b = Buliding(4)
print (b)

b.occupy(0,'Reception')
b.occupy(1,'ABC Corp')
print (b)
print (b.get_floor_data(0))

#############################################################

class Buliding1(object):
	def __init__(self, floors):
		self._floors = [None]*floors

	def __setitem__(self, floors_number, data):
		self._floors[floors_number] = data

	def __getitem__(self, floors_number):
		return self._floors[floors_number]

	def __repr__(self):
		s=''.join([str(s) for s in self._floors])
		return s

b1 = Buliding1(5)
b1[0] = 'Reception'
b1[1] = 'cofe'

print (b1)
print (b1[1])

#############################################################

class Indexer:
	def __getitem__(self, index):
		return index**2

x = Indexer()
y = x[2]
print ('='*30)
print (y)

#############################################################

class Indexer1(object):
	data = [5,6,7,8,9]
	
	def __setitem__(self, index, value): # Реализует присваивание
		self.data[index] = value # присваивание по индексу или по срезу
	
	def __getitem__(self, index): # вызывается при индексировании
		print ('Getitem : ',index) # извлечении среза
		return self.data[index] # выполяет индексирование

Y = Indexer()
print ('*'*30)
print (Y[0]) # 5
xx = Y[1]
print (xx)



