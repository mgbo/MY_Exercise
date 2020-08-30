
import turtle

def tri(t,x,color):
	
	ang=60
	t.pencolor(color)
	

	t.fd(x)
	
	t.left(180-ang)
	t.forward(x)
	
	t.left(180-ang)
	t.forward(x)
	
	#t.right(120)

def turn(ang):
	
	t.right(120)
	
	

t=turtle.Turtle()
t.width(3)
t.shape("turtle")

tri(t,50,'green')

#t.right(120)
turn(70)
tri(t,100,'red')

#t.right(120)
turn(90)
tri(t,100,'blue')
turn(60)


turtle.mainloop()
