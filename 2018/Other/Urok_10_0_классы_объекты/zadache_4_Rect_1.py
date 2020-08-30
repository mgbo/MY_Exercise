
from zadache_3_Point import Point

class Rect:
	""" прямоугольник со сторонами, параллельными осям X и Y"""
	def __init__(self, lt=Point(), rb=Point()):
		self.lt = lt
		self.rb = rb

	def printR(self):
		print("("+str(self.lt),str(self.rb)+")")

	def __str__(self):
		#return str(self.lt)+' '+str(self.rb)
		return "({},{})".format(str(self.lt),str(self.rb))

	def read_Rec(self):
		self.lt.read()
		self.rb.read()

	def center(self):
		#p = Point()
		w = (self.rb.x - self.lt.x)
		h = (self.lt.y - self.rb.y)
		#return Point(self.lt.x + w/2, self.lt.y - h/2)
		return (self.lt.x + abs(w/2), self.lt.y - abs(h/2))

	def set(self, lt, rb):
		self.lt = lt
		self.rb = rb

	def moveTo(self, a):
		#сдвигает прямоугольник так, чтобы его центр был в точке а
		R_n = Rect()

		w = (self.rb.x - self.lt.x)/2
		h = (self.lt.y - self.rb.y)/2

		print ("C_P : ",w,",",h)

		R_n.lt.x = a.x - w
		R_n.rb.x = a.x + w

		R_n.lt.y = a.y + h
		R_n.rb.y = a.y - h

		return R_n

	def flipH(self):
		#отображает прямоугольник относительно оси ОX
		R_h = Rect()

		y_lt = -(self.rb.y)
		y_rb = -(self.lt.y)

		R_h.lt.y = y_lt
		R_h.rb.y = y_rb

		return R_h

	def flipV(self):
		R_v = Rect()

		x_lt = -(self.rb.x)
		x_rb = -(self.lt.x)

		R_v.lt.x = x_lt
		R_v.rb.x = x_rb

		return R_v

	def rot90(self):
		R_90 = Rect()
		c_x,c_y = R_90.center()
		print ("центр прямоугольника находиться в точке ({},{})".format(c_x,c_y))
		
		dx = c_x - self.lt.x
		print ("dx : ",dx)

		dy = self.lt.y - c_y
		print ("dy : ",dy)

		R_90.lt.x = c_x - dy
		R_90.lt.y = c_y + dx

		R_90.rb.x = c_x + dy
		R_90.rb.y = c_y - dx

		return R_90

	def cross(self,rect):
		if (self.rb.y>rect.lt.y or self.lt.y<rect.rb.y or self.lt.x>self.rb.x or self.rb.x<rect.lt.x):
			return None
		else:
			return rect

if __name__ == '__main__':
	R1 = Rect()
	R2 = Rect()

	R1.read_Rec()
	R2.read_Rec()

	R1.printR()
	R2.printR()
	
	'''
	R1 = Rect()
	R1.set((1,5),(7,1))
	

	R2 = Rect()
	print ("Введите точки для прямоугольник : ")
	R2.read_Rec()
	print (R2)
	print (R1)


	"""____ Возращает точку - центр прямоугольника ____"""
	p = R2.center() 
	print(p)

	"""-------- сдвигает пррямоугольник так,
	чтобы центр бы в точке а """
	R_move = R2.moveTo(Point(4,-3))
	print("NEW Position : ",R_move)
	
	R3 = Rect()
	R3.read_Rec()

	R_hh = R3.flipH()
	print ('\n\n')
	print(R_hh)

	R4 = Rect()
	R3.read_Rec()
	R_vv = R4.flipV()
	print (R_hh)
		R_90 = Rect()
	R_99 = Rect()
	R_90.read_Rec()
	print (R_90)

	#ans_90 = R_90.rot90()
	#print (ans_90)
	R_99.read_Rec()

	print (R_90)
	print (R_99)

	Cro_Ret = R_90.cross(R_99)
	print (Cro_Ret)
	'''



































