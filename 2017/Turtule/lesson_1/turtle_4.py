

import turtle 

t=turtle.Turtle()

t.shape("turtle")

x=75
ang=90

t.width(5)

t.pencolor("green")

t.forward(x)
t.left(ang)

t.forward(x)
t.left(ang)

t.forward(x)
t.right(-ang)

t.forward(x)

turtle.mainloop()
