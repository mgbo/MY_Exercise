import turtle

t=turtle.Turtle()

def shape(side,length):
	t.lt(45)
	for _ in range(side):
		t.lt(360/side)
		t.fd(length)	
side=3
length=50
delta=10

for _ in range (10):
	shape(side,length)
	t.up()
	t.rt(45)
	t.fd(delta)
	t.down()
	side+=1
	length+=delta;
	
turtle.done()
