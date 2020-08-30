
import turtle

m = map(int, input().split())

t = turtle.Turtle()

def data(nn):
	t.write((nn), font=("Arial", 14, "normal"))

y = 0
i = 0
res = 0

for ii in m:
	res += ii
	i += 1
	t.fd(ii)
	data(ii)
	y+=30
	t.penup()
	t.goto(0,-y)
	t.pendown()
	
t.color('red')
t.fd(res//i)
data(res//i)

turtle.done()

