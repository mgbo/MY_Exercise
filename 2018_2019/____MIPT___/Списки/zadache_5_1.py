
import turtle
import sys
import math

# t = turtle.Turtle()
ip = sys.stdin

ind = int(input("Номер индекс : "))
print (ind)

lis_p = []

def list_p():
	for i in ip:
		x, y = map(int, i.split())
		lis_p.append((x,y))
	return lis_p


l = list_p()
b = l.copy()
print (l)
l.pop()

print (l)

print (b)
# turtle.done()

if __name__ == '__main__':
	a = 5


