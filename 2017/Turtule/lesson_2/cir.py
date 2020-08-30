
import turtle

t=turtle.Turtle()

t.color('red','magenta')

t.begin_fill()

t.speed('fastest')
i=0
while i<=32:
	t.lt(11.25)
	t.fd(20)
	i+=1
	
t.end_fill()

t.up()
t.fd(200)
t.down()

j=0
while j<=360:
	t.fd(20)
	t.bk(20)
	t.lt(1)
	j+=1

t.hideturtle()

turtle.done()
