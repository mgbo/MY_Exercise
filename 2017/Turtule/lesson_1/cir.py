
import turtle

def cir():
	
	#x=700
	#y=400
	#turtle.setup(x,y)
	turtle.penup()
	turtle.goto(0,0)
	
	t=turtle.Pen()
	t.pendown()
	
	t.begin_fill()
	t.circle(80)
	t.color("green")
	t.end_fill()
	
	t.hideturtle()
	turtle.done()
	
cir()

	
