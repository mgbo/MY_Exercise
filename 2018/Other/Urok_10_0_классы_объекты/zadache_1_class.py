
class Time12():
	
	# конструктор класса имеет специальное имя __init__ по умочанию сделаем время 00:00
	def __init__(self, h=0, m=0):
		self.h = h # часы от 0 до 11
		self.m = m # минуты от о до 59
		# self.set()

	def __str__(self):
		return "%02d:%02d"% (self.h, self.m)

	def set(self, h24=0, m24=0):
		if h24<0 or h24>=24 or m24<0 or m24>=60:
			raise ValueError("No good : hour = %d  min = %d "% (h24, m24))
		# self.m = m24
		# self.h = h24

	def add(self, dt):
		m = self.m + dt.m
		''' sef.m минуты ЭТОГО объекта, dt.m минуты переданного объекта типа 
		'''
		self.m = m % 60
		self.h = (self.h + dt.h + m//60) % 12
	
	def sub(self, dt):
		m = self.m + (self.h)*60
		m_dt = dt.m + dt.h*60

		if m_dt < m:
			m +=24*60

		self.m = (m - m_dt) % 60
		self.h = ((m - m_dt)//60)%12

	def compare(self, t):
		m_t = t.m + t.h*60
		#print ("m_t : ",m_t)

		m_o = self.m + self.h * 60
		#print ("m_o : ",m_o)

		if m_t==m_o:
			return 0

		elif m_o>m_t:
			return 1

		else:
			return -1


	def round(self):
		t = Time12()

		t.h = self.h

		if self.m>0:
			t.h = (t.h + 1)%12

		print("round : ",t)
		return t

if __name__ == "__main__":
	
	t1 = Time12(11,5)
	print(t1)


	t2 = Time12(11,15)
	print(t2)

	#t1.sub(t2)
	#t1.print()

	ans = t1.compare(t2)
	print (ans)

	t3 =Time12(15, 35)
	tt = t3.round()
	print(tt, type(tt))














