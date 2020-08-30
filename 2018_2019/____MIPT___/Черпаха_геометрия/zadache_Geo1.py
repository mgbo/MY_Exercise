
'''
rect(x1, y1, x2, y2)
прямоугольник по левой верхней (x1, y1)
правой нижней точкам (x2, y2)
'''
import turtle

fb = ("Arial", 14, "normal")

# рисуем отрезок с канцами (x1,y1) и (x2,y2)
def line(x1, y1, x2, y2):
	t.pu()
	t.setpos((x1,y1))
	t.pd()
	t.setpos((x2,y2))

def rect(x1, y1, x2, y2):
	line(x1, y1, x2, y1)
	line(x2, y1, x2, y2)
	line(x2, y2, x1, y2)
	line(x1, y2, x1, y1)

t = turtle.Turtle()
t.width(5)
t.color('blue')

rect(0, 100, 200, 0)

turtle.done()



