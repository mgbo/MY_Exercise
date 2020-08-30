
import turtle

wn = turtle.Screen()
wn.bgcolor('red')
wn.title("simple python turtle graphics")


class Player(turtle.Turtle):
	def __init__(self, spriteshape, color):
		turtle.Turtle.__init__(self, shape = spriteshape)
		self.penup()
		self.color(color)
		self.speed = 1
		# self.shape(spriteshape)
		

	def move(self):
		self.fd(self.speed)

player = Player('square', 'white')


while True:
	player.move()

turtle.done()