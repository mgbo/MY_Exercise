import turtle

def square(t,x,color,w):
	
	ang=90
	t.pencolor(color)
	t.width(w)
	
	t.forward(x)
	t.left(ang)
	
	t.forward(x)
	t.left(ang)
	
	t.forward(x)
	t.left(ang)
	
	t.forward(x)
	t.left(ang)

t=turtle.Turtle()

t.begin_fill()
t.color("green")
square(t,75,'green',5)
turtle.position()
t.end_fill()

#square(t,50,'red',3)

turtle.mainloop()
