
import turtle

fb = ("Arial", 14, "normal")

# передвигаем черепаху в точку (x,y), не рисуем
def goto(x,y):
	t.pu()
	t.setpos((x,y))

# рисуем отрезок с канцами (x1,y1) и (x2,y2)
def line(x1, y1, x2, y2):
	t.pu()
	t.setpos((x1,y1))
	t.pd()
	t.setpos((x2,y2))

t = turtle.Turtle()
t.width(5)
t.color('blue')
t.speed(1)
# рисуем треугольник 
# линии можно рисовать в любом порядке

line(30, -50, 200, 0)
line(30, -50, 100, 150)
line(200, 0, 100, 150)

turtle.done()

