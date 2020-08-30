
'''
mycolors = ['blue', 'red', 'green', 'gold', 'violet', 'orange', 'yellow']
letters = ['b', 'r', 'gr', 'gl', 'v', 'o', 'y']

let = 'v'


for ilet in range(len(letters)):
	if letters[ilet] == let:
		break

col = mycolors[ilet]
# print (col)
'''

import turtle

def sq(x, y, size):
	t.pu()
	t.goto(x, y) # начальная координата
	t.pd()

	t.begin_fill()
	for i in range(4):
		t.fd(size)
		t.rt(90)
	t.end_fill()

def read_and_draw_1sq():
	x, y, size, a = input().split()
	x = int(x)
	y = int(y)
	size = int(size)
	
	t.color(dcolors[a])
	sq(x, y, size)


t = turtle.Turtle()
t.width(5)

# писали РАНЬШЕ списки
mycolors = ['blue', 'red', 'green', 'gold', 'violet', 'orange', 'yellow']
letters =  ['a',     'b',    'c',    'd',    'v',      'o',      'z']

# теперь пишем словарь
dcolors = {
	'a': 'blue',
	'b': 'red',
	'c': 'green',
	'd': 'gold',
	'v': 'violet',
	'o': 'orange',
	'z': 'yellow'
}

n = int(input()) # количесво квадратов


for i in range(n):
	read_and_draw_1sq()

turtle.done()



