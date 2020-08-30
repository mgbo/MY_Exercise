
import turtle
import time
import math

oboi = turtle.Screen()
t = turtle.Turtle()

oboi.bgcolor("grey")
colors = ['blue','red','magenta','violet','purple','cyan','green']

t.speed(0)
for angle in range(0,360,15):
	t.color(colors[angle%7])
	t.seth(angle)
	t.circle(100)
	
#t.reset()
#turtle.mainloop()
oboi.exitonclick()
