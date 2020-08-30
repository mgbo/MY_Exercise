
import turtle

t = turtle.Turtle()
t.width(5)

dcolors = {
	'a': 'blue',
	'b': 'red',
	'c': 'green',
	'd': 'gold',
	'v': 'violet',
	'o': 'orange',
	'z': 'yellow'
}

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


n = int(input("Введите количесто квадратов : "))

for i in range(n):
	read_and_draw_1sq()

turtle.done()


















