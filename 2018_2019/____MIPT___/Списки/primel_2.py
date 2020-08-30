
import turtle
import sys


fp = sys.stdin

t = turtle.Turtle()

t.color('darkgreen')

for string in fp:
	x, y = map(int,string.split())
	t.setpos((x,y))

turtle.done() 