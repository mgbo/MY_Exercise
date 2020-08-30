 
import turtle

t = turtle.Turtle()
t.width(5)

def line(s):
	t.lt(90)
	t.fd(s)


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
l.sort(key= lambda l: int(l[1]))
# print (l)

for i in range(len(l)):
	print (l[i][0], l[i][1])
	col = l[i][0]
	size = int(l[i][1])

	x = t.xcor()
	y = t.ycor()

	t.pencolor(col)
	line(size)
	t.pu()
	t.goto(x,y)

	t.rt(90)
	t.fd(50)
	t.pd()


turtle.done()






