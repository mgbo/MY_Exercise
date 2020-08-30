

import turtle

t = turtle.Turtle()
t.width(5)

def create_dcolor(n):
	dcolors = {}
	for i in range(n):
		val, key = input().split()

		if val not in dcolors:
			dcolors[val] = key

	return dcolors


	
def sq(x, y, size):
	t.penup()
	t.goto(x, y)
	t.pendown()

	t.begin_fill()

	for i in range(4):
		t.fd(size)
		t.rt(90)

	t.end_fill()

def read_and_draw_1sq():
	x, y, size, col_1, col_2 = input().split()

	x = int(x)
	y = int(y)

	size = int(size)

	t.pencolor(dcolors[col_2])
	t.fillcolor(dcolors[col_1])


	sq(x, y, size)

n = int(input("Количество цветов : "))
dcolors = create_dcolor(n)

nn = int(input("Количество квадратов"))

for i in range(nn):
	read_and_draw_1sq()



turtle.done()









