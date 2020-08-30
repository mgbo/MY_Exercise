
import turtle

t=turtle.Turtle()

t.shape("circle")
x=75
ang=90

t.forward(x)
t.left(ang)
t.forward(x)
t.right(ang)

x=50
t.forward(x)
t.left(ang)
t.forward(x)
t.right(ang)

x=x-5

t.forward(x)
t.left(ang)
t.forward(x)
t.right(ang)

t.forward(x)
t.left(ang)
t.forward(x)
t.right(ang)

t.forward(x)
t.left(ang)
t.forward(x)
t.right(ang)
turtle.mainloop()
