
from grid import Grid

class Segment:
	def __init__(self, x1, x2):
		self.start = x1
		self.finish = x2


	def __repr__(self):
		d = self.length()
		return f'отрезок [{self.start}, {self.finish}] длины {d}'

	def length(self):
		return self.finish - self.start

	def draw(self, col='blue'):
		g.draw_line(self.start, 0, self.finish, 0, col)

	def move(self, dx):
		self.start = self.start + dx
		self.finish = self.finish + dx


g = Grid()

s = Segment(0, 50)
print (s)
s.draw()

s.move(50)
s.draw()

s2 = Segment(-70, -20)
s2.draw()

g.done()












