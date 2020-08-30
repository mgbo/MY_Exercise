
import turtle



def sq(x, y, size, filling):
	t.pu()
	t.goto(x, y)
	t.pd()

	if filling:
		t.begin_fill()

	for i in range(4):
		t.fd(size)
		t.rt(90)

	if filling:
		t.end_fill()

d = {} # 

def read_and_draw_lsq():
	x, y, size, col = input().split()
	x = int(x)
	y = int(y)
	size = int(size)

	t.color(col)

	# print (x, y, size, col)

	sq(x, y, size, filling=False)

	d[col] = [x, y, size] # добавить элементы(key & value) в dict


t = turtle.Turtle()
t.width(5)

n = int(input())

for i in range(n):
	read_and_draw_lsq()

print ("dict --> {}".format(d))



for c in d: # только ключ
	kv = d[c] # забрать значение по ключу
	print (c, ':', kv)
	t.color(c)
	sq(kv[0], kv[1], kv[2], filling=True)


turtle.done()









