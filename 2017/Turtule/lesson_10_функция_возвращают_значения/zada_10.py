
#-*- coding:utf-8 -*-
import turtle
import time

def branch(n,size0,dsize,dang):
	
t=turtle.Turtle()
t.width(3)
t.shape('turtle')

for i in range(3):
   pc = branch(6, 50, 5, 20, 10)     # ветка вверх
   t.up()
   t.goto(pc)
   pc = branch(6, 50, 5, -20, -10)   # ветка вниз
   t.up()
   t.goto(pc)

turtle.done()
