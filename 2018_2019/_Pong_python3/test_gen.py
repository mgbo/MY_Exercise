
import turtle

# t = turtle.Turtle()
t = turtle.Screen()
t.setup(width=800, height=600)
t.tracer(0)

# t.lt(60)
# t.fd(100)
# print (t.pos()) # узнаем координат

# def f():
# 	t.fd(50)
# 	t.lt(60)

# t.onkey(f, "Up")
# t.listen()


# t.dx = 200
# print (t.xcor()) # узнаем координат



# turtle.done()

# pen
pen = turtle.Turtle()
pen.speed(0)
pen.color('red')
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write("Player A: 0", align='center', font=('Arial', 26, 'normal'))
# pen.clear()

while True:
	t.update()










