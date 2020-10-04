
from grid import Grid, Point, Rectangle

g = Grid()


class Point:
	def __init__(self, x, y, col='blue'):
		self.x = x
		self.y = y
		self.col = col

	def draw(self):
		g.draw_dot(self.x, self.y, self.col)

p1 = Point(0,0, 'red')
p1.draw()

g.done()
