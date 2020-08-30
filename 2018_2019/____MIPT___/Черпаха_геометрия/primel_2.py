
import turtle


fb = ("Arial", 16, "normal")

def goto(x, y):
	t.pu()
	t.setpos((x,y))

def line(x1, y1, x2, y2):
	t.pu()
	t.setpos((x1, y1))
	t.pd()
	t.setpos((x2, y2))

t = turtle.Turtle()
t.width(5)
t.color('blue')


line(30, -50, 200, 0)

turtle.done()

