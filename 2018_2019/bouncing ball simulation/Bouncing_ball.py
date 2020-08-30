
# bouncing ball simulation

import turtle
from random import*


s = turtle.Screen()
s.bgcolor('black')
s.title('Bouncing Ball')
s.tracer(0)

balls = []
colors = ['magenta', 'red', 'green', 'yellow', 'blue', 'orange', 'white', 'purple']
shapes = ['triangle', 'circle', 'square']

for _ in range(30):
	balls.append(turtle.Turtle())


for b in balls:
	b.shape(choice(shapes))
	b.color(choice(colors))
	b.penup()
	b.speed(0)
	x = randint(-290,290)
	y = randint(200,400)

	b.goto(x, y)
	b.dy = 0
	b.dx = 2
	gravity = 0.1
	b.da = 0


while True:
	s.update()

	for b in balls:
		b.dy -= gravity

		xx = b.xcor() + b.dx
		yy = b.ycor() + b.dy
		# print (xx, yy)
		b.goto(xx,yy)

		if b.xcor() < -300:
			b.dx *=-1
			b.da += 45

		if b.xcor() > 300:
			b.dx *=-1
			b.da +=10

		########### Check for a bounce ##########
		if b.ycor() < -300:
			b.dy *= -1
			b.da +=45





turtle.mainloop()


