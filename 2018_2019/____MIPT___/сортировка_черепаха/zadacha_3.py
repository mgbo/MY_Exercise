 
import turtle

t = turtle.Turtle()
t.width(5)

def line(size, col):
	t.pencolor(col)
	t.lt(90)
	t.fd(size)

def input_data(n):
	l = []
	for i in range(n):
		s, c = input().split()
		l.append((s,c))

	return l

def line(size):
	t.lt(90)
	t.fd(size)


n = int(input())
l = input_data(n)
l.sort(key= lambda l: int(l[0]))
# print (l)

for s, c in l:
	# print (s, c)
	x = t.xcor()
	y = t.ycor()

	t.pencolor(c)
	t.lt(90)
	t.fd(int(s))
	

	t.pu()
	t.goto(x,y)

	t.rt(90)
	t.fd(50)
	t.pd()



turtle.done()



