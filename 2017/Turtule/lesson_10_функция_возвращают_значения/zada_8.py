#-*- coding:utf-8-*-
import turtle
import time
import math 

def write(data):
	t.write(data, font=("Arial",14,"normal"))

def carre(size,col):
	t.color('gold',col)
	t.begin_fill()
	for i in range(4):
		t.fd(size)
		t.lt(90)
	t.end_fill()

def carreInf(size,skolko):
	count=0
	while skolko>0 and skolko>0:
		if size>0:
			if skolko% 3 == 0:
				col = "darkgreen"
			elif skolko%3 == 1:
				col = "yellow"
			else:
				col="red"
			d = math.sqrt(10*10+10*10)
			print (d)
			t.down()
			carre(size,col)
			#write(size)
			t.up()
			t.lt(45)
			t.fd(d)
			t.seth(0)
			size-=20
			count+=1
		skolko-=1
	return count

t=turtle.Turtle()
t.width(3)
PP = carreInf(100,5)
t.up()
t.goto(0,200)
t.down()
write(PP)
turtle.done()
