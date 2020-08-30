
import turtle



def square(t, length):
	for i in range(4):
		t.fd(length)
		t.lt(90)

bob = turtle.Turtle()
square(bob, 100)

tt = turtle.Turtle()
tt.penup()
tt.goto(-100,0)

tt.pendown()
tt.shape('turtle')
tt.color('red')
square(tt, 100)
turtle.done()
