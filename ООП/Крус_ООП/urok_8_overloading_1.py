
class Changeable:
	def __init__(self, color):
		self.color = color

	def __call__(self, newcolor):
		self.color = newcolor

	def __str__(self):
		return "%s"% self.color


canvas = Changeable("green")
frame = Changeable("blue")

canvas("red")
canvas("yellow")

print (canvas, frame)



