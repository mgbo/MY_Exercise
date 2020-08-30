
import turtle

t=turtle.Turtle()

t.color('red','yellow')

t.begin_fill()

i=0

t.rt(90)
while i<=4:
 t.rt(144)
 t.fd(100)
 i+=1

t.end_fill()
turtle.mainloop()

