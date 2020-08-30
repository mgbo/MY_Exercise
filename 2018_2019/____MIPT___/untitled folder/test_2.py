
import turtle

t = turtle.Turtle()

m = map(int, input().split())

def turn(y):
	y = 0
	y+=30
	t.penup()
	t.goto(0,-y)
	t.pendown()

def write(n):
	t.write((n), font=("Arial", 14, "normal"))

y = 0
for x in m:
	y += 30
	t.fd(x)
	write(x)


turtle.done()