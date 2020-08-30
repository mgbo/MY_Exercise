
import turtle

def square(t):
	x=75
	ang=90
	
	t.forward(x)
	t.left(ang)
	
	t.forward(x)
	t.left(ang)
	
	t.forward(x)
	t.left(ang)
	
	t.forward(x)
	#t.left(ang)
	
t=turtle.Turtle()
t.shape("turtle")


square(t)
t.right(90)

square(t)

turtle.mainloop()
	
