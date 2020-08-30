
import turtle

t=turtle.Turtle()

i=0
t.shape("turtle")
t.pencolor("red")

t.width(5)

t.pendown()
t.stamp()

while i<=360:
	
	
	t.forward(200)
	t.backward(200)
	
	t.right(i)
	i+=30
	
#t.backward(200)
#t.circle(200)

turtle.mainloop()
