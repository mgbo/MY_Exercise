
import turtle

def tri(t,x):
	
	ang=60
	
	t.forward(x)
	t.left(180-ang)
	
	t.forward(x)
	t.left(180-ang)
	
	t.forward(x)
	t.left(180-ang)

t=turtle.Turtle()

t.width(3)
t.pencolor("green")

tri(t,200)

t.pencolor("red")
tri(t,100)

turtle.mainloop()
