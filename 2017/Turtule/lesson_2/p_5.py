
import turtle

t=turtle.Turtle()
t.width(3)
t.color('red','magenta')

t.begin_fill()
i=0

while i<=5:
	
	t.fd(100)
	t.lt(72)
	i+=1


t.end_fill()
turtle.mainloop()

