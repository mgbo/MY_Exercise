
class Time():
	def __init__(self, h=0, m=0):
		self.h = h
		self.m = m

	def __str__(self):
		return "%02d:%02d"% (self.h, self.m)

	def set(self, h24=0, m24=0):
		if h24<0 or h24>=24 or m24<0 or m24>=60:
			raise ValueError("hour and minutes do not exits")

	def add(self, dt):
		m = self.m + dt.m
		''' sef.m минуты ЭТОГО объекта, dt.m минуты переданного объекта типа 
		'''
		self.m = m % 60
		self.h = (self.h + dt.h + m//60) % 12

	def compare(self, t):
		m_t = t.m + t.h*60
		print ("m_t : ",m_t)

		m_o = self.m + self.h * 60
		print ("m_o : ",m_o)

		if m_t==m_o:
			return 0
		elif m_o>m_t:
			return 1
		elif m_o<m_t:
			return -1

	def SameTime(self,t):
		s_t = Time()

		m_t = t.m + t.h * 60
		m_o = self.m + t.h * 60

		for i in range(1,25):
			m_t = (m_t + 30)%720

			m_o = (m_o - 60)%720

			print (m_t,m_o)
			if abs(m_t)==abs(m_o):
				s_t.m = abs(m_t%60)
				s_t.h = abs(m_t//60)
				return s_t
				break
	'''
	def sameTime(t1, dt1, dt2):
		t2 = Time()
		t2.h = t1.h
		t2.m = t1.m
		#t2 = copy.copy(t1)

		every = Time(0, 30) 

		k = 0
		while True:
			k += 1
			t1.add(every)
			t1.add(dt1)

			t2.add(every)

			if k % 2 == 0:
				t2.sub(dt2)
			if t1.compare(t2) == 0:
				break
	'''

if __name__ == "__main__":
	t1 = Time(1,30)
	t2 = Time(12,30)

	print (t1)
	print (t2)

	ans = t1.compare(t2)
	print (ans)

	t3 = Time()
	t3 = t1.SameTime(t2)
	print(t3)






















