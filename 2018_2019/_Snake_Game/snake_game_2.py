
'''
Simple Snake Game in python3 for Beginners
Part 2: Snake Head
'''
import turtle
import time

delay = 0.1

# set up the screen
wn = turtle.Screen()
wn.title("Snake Game")
wn.bgcolor('green')
wn.setup(width=600, height=600)
wn.tracer(0) # turn off the screen updates


# Snake head
head = turtle.Turtle()
head.speed(0)
head.shape('square')
head.color('black')
head.penup()
head.goto(0,0)
head.direction = 'stop'


# Function
def go_up():
	head.direction = 'up'

def go_down():
	head.direction = 'down'

def go_left():
	head.direction = 'left'
	
def go_right():
	head.direction = 'right'
	

def move():
	if head.direction == 'up':
		y = head.ycor()
		head.sety(y + 20)

	if head.direction == 'down':
		y = head.ycor()
		head.sety(y - 20)

	if head.direction == 'left':
		x = head.xcor()
		head.setx(x - 20)

	if head.direction == 'right':
		x = head.xcor()
		head.setx(x + 20)

# Keyboard bindings
wn.listen()
wn.onkeypress(go_up, 'Up')
wn.onkeypress(go_down, 'Down')
wn.onkeypress(go_left, 'Left')
wn.onkeypress(go_right, 'Right')


# Main game loop
while  True:
	wn.update()

	move()
	time.sleep(delay)

turtle.mainloop()





