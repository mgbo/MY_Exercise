
import turtle

t=turtle.Turtle()

i=0
t.color('red')
t.width(3)

while i<=3:
	t.fd(50)
	t.up()
	t.fd(25)
	t.down()
	i+=1

t.hideturtle()
turtle.done() 
