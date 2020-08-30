
class Time12():
	# конструктор класса имеет специальное имя __init__ по умочанию сделаем время 00:00
	def __init__(self, h=0, m=0):
		self.h = h # часы от 0 до 11
		self.m = m # минуты от о до 59

	def __str__(self):
		return "STR %02d:%02d"% (self.h, self.m)

	def print(self):
		print ("%02d:%02d"% (self.h, self.m))
		
	def set(self, h24=0, m24=0):
		if h24<0 or h24>=24 or m24<0 or m24>=60:
			raise ValueError("hour = %d  min = %d "% (h24, m24))
		self.m = m24
		self.h = h24

	def add(self, dt):
		m = self.m + dt.m
		''' sef.m минуты ЭТОГО объекта, dt.m минуты переданного объекта типа 
		'''
		self.m = m % 60
		self.h = (self.h + dt.h + m//60) % 12

	def round(self):
		t = Time12()

		t.h = self.h

		if self.m>0:
			t.h = (t.h + 1)%12
		return t

if __name__ == "__main__":
	 # как можно использовать этот класс (и его нужно протестировать!)

	 t1 = Time12(1,0)
	 t1.print()
	 
	 t2 = Time12()
	 t2.set(2,5)

	 print(t2)















