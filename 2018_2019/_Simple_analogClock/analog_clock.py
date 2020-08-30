
# Simple Analog Clock in python3
# by @TokyoEdTech
# Part 1: Getting Started

import turtle
import time

wn = turtle.Screen()
wn.bgcolor('black')
wn.setup(width=600, height=600)
wn.title("Simple Analog Clock by @TokyoEdTech")
wn.tracer(0)

# create our drawing pen
pen = turtle.Turtle()
pen.hideturtle() # Не показывать черепаху
pen.speed(0)
pen.pensize(3)


t = turtle.Turtle()
t.penup()
t.goto(0,250)
t.pendown()
t.hideturtle()
t.color('blue')
t.write("This is my first clock", align='center', font=('Arial', 20, 'normal'))

def draw_clock(h, m, s, pen):
	# draw clock face
	pen.up() # НЕ рисовать когда движется turtle.penup()/ turtle.pu()
	pen.goto(0,210)
	pen.setheading(180) # повернуть черепаху на n градусов
	pen.color("green")
	pen.pendown()
	pen.circle(210)

	# Draw the lines for the hours
	pen.penup()
	#pen.showturtle()
	pen.goto(0,0)
	pen.pendown()
	pen.setheading(90)

	for _ in range(12):
		pen.up()
		pen.fd(180)
		pen.pendown()
		pen.fd(20)
		pen.penup()
		pen.goto(0,0)
		pen.rt(30)

	# Draw the hour hand
	pen.penup()
	pen.goto(0,0)
	pen.color('white')
	pen.setheading(90)
	angle = (h/12) * 360
	pen.rt(angle)
	pen.pendown()
	#pen.shape('arrow')
	pen.fd(100)

	# Draw the minutes hand
	pen.penup()
	pen.goto(0,0)
	pen.color('red')
	pen.setheading(90)
	angle = (m/60) * 360
	pen.rt(angle)
	pen.pendown()
	pen.fd(120)

	# Draw the seconds hand
	pen.penup()
	pen.goto(0,0)
	pen.color('blue')
	pen.setheading(90)
	angle = (s/60) * 360
	pen.rt(angle)
	pen.pendown()
	pen.fd(180)


while True:
	h = int(time.strftime("%I"))
	m = int(time.strftime("%M"))
	s = int(time.strftime("%S"))

	draw_clock(h, m, s, pen)
	wn.update()
	#time.sleep(1)

	pen.clear()

# draw_clock(6, 15, 45, pen)



wn.mainloop() # Конец работы черепахи. Окно не закрывать.







