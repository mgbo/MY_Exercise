
import turtle

t = turtle.Turtle()
t.color('blue')
t.width(5)

def line(size):
	t.lt(90)
	t.fd(size)


l = list(map(int, input().split()))
l.sort(reverse=True)

for s in l:
	x = t.xcor()
	y = t.ycor()

	line(s)

	t.pu()
	t.goto(x,y)

	t.rt(90)
	t.fd(50)
	t.pd()
	



turtle.done()
