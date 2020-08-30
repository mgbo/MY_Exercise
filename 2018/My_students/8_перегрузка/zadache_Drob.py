
""" Напишите класс Drob, который представляет дроби в виде целых числителя и знаменателя."""

def nod(a,b): # наибольший общий делитель (НОД)
	rest = 1
	while rest!=0:
		rest = a % b
		#print (rest)
		a,b = b,rest
		#print (a,b)
	return a

class Drob(object):
	""" Дробь вида a/b """
	def __init__(self, a=0, b=1):
		self.a = a
		self.b = b
		self.nomalize()

		if self.b < 0:
			self.b = abs(self.b)
			self.a = -1*self.a
		elif self.b == 0:
			raise ZeroDivisionError

	def nomalize(self):
		""" Приводит дробь вида 4/6 к 2/3"""
		self.a, self.b = self.a//nod(abs(self.a),abs(self.b)), self.b//nod(abs(self.a), abs(self.b))

	def __str__(self):
		if self.b == 1:
			return '{}'.format(self.a)
		else:
			return '{}/{}'.format(self.a, self.b)

	def __repr__(self):
		#return '({}/{})'.format(self.a, self.b)
		return self.__str__()

	def __eq__(self, other):
		return self.a == other.a and self.b == other.b

	def __lt__(self, other):
		return self.a * other.b < self.b * other.a

	def __gt__(self, other):
		return self.a * other.b > self.b* other.a

	def __add__(self, other):
		t = Drob()
		t.a = (self.a * other.b) + (self.b * other.a)
		t.b = (self.b * other.b)
		t.nomalize()
		return t

	def __sub__(self, other):
		t = Drob()
		t.a = (self.a * other.b) - (self.b * other.a)
		t.b = (self.b * other.b)
		t.nomalize()
		return t

	def __floordiv__(self, other):
		d_new = Drob()
		# return (self.a * other.b)//(self.b * other.a)
		d_new.a = self.a * other.b
		d_new.b = self.b * other.a

		d_new.nomalize()
		return d_new

	def __truediv__(self, other):
		d_new = Drob()
		d_new.a = self.a * other.b
		d_new.b = self.b * other.a
		d_new.nomalize()
		return d_new

	def __mul__(self, other):

		t_n = Drob()
		t_n.a = (self.a * other.a)
		t_n.b = (self.b * other.b)

		t_n.nomalize()

		return t_n

	def __pow__(self, n):

		aa = self.a ** n
		bb = self.b ** n

		return Drob(aa,bb)


def test():

	d1 = Drob(1,2)
	print (d1)
	d2 = Drob(3,4)
	print (d2)

	# -------------- lt ------------------------
	print (d1<d2) # True
	print (d1>d2) # False

	#---------------- gt ----------------------
	print(Drob(9,2)>Drob(5,2)) # True

	#---------------- add ---------------------
	print(Drob(5,2)+Drob(10,3)) # 35/6

	#---------------- sub ----------------------
	print(Drob(19,5)-Drob(2,3)) # 47/15

	#---------------- mul ----------------------
	print (Drob(2,4)*Drob(2,3)) # 4/12 --> 1/3

	#---------------- floordiv ------------------
	print (Drob(2,3)//Drob(2,3))

	#--------------- div ------------------------
	print (Drob(2,3)/Drob(2,3))

	#---------------- floordiv ------------------
	print (Drob(2,4)**2)


if __name__ == "__main__":

	test()


	#a,b = map(int, input().split())
	#print (nod(a,b))
	print ("-------------")
	f1 = Drob(2,-3)
	f2 = Drob(2,4)
	f3 = f1+f2
	print (f3,type(f3))
	print ("-----------")

	d1 = Drob(2,4)
	print (d1)

	d2 = Drob(2,3)
	print (d2)

	print ("ANS :",d1*d2)


	d3 = Drob(18,-2)
	print (d3)
	
	print ('------')
	print (Drob(1/3) + Drob(1/6))
