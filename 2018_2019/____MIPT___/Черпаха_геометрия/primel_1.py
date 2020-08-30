
import turtle

t = turtle.Turtle()
t.width(5)

fb = ("Arial", 16, "normal")

def goto(x, y):
	t.pu()
	t.setpos((x,y))


t.fd(100)
t.lt(90)
t.fd(50)


p = t.pos()
t.write(p, font=fb)

turtle.done()

