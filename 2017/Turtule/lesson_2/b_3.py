
import turtle

t=turtle.Turtle()

t.shape("turtle")
t.width(3)
t.pencolor("blue")

t.fd(100)

t.lt(90)
t.fd(50)
t.bk(100)

turtle.speed()
t.hideturtle()
ans=t.pos()
print (ans)
turtle.done()
