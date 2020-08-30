
'''
rect(x1, y1, xс, yс)
прямоугольник по левой верхней (x1, y1) точке и пересечению диагоналей (xc, yc)
'''

import turtle

fb = ('Arial', 10, 'normal')

def line(x1, y1, x2, y2):
	t.pu()
	t.setpos((x1, y1))
	t.pd()
	t.setpos((x2, y2))
	polo = t.pos()
	t.write(polo, font=fb)

def rect(x1, y1, x2, y2):
	line(x1, y1, (-(x1-x2)+x2), y1)
	line((-(x1-x2)+x2), y1, (-(x1-x2)+x2), (-(y2-y1)))
	
	line((-(x1-x2)+x2), (-(y2-y1)), x1, (-(y2-y1)) )
	line(x1, (-(y2-y1)), x1, y1)
	

t = turtle.Turtle()
t.width(5)
t.color('blue')

rect(-500,300, -250,150)

turtle.done()



