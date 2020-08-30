
# Falling Skies in Python 3 for the Begineers

import turtle
import random

score = 0
lives = 1

wn = turtle.Screen()
wn.title("Falling Skies")
wn.bgcolor("green")
wn.bgpic('bk1.gif')
wn.setup(width=800, height=600)
wn.tracer(0)

wn.register_shape('para.gif')
wn.register_shape('tank.gif')

# Add the player
player = turtle.Turtle()
player.speed(0)
player.shape("tank.gif")
player.color('white')
player.penup()
player.goto(0,-250)
player.direction = 'stop'


# Create a list of good guys
good_guys = []

# Add the good_guy
for _ in range(20):
	good_guy = turtle.Turtle()
	good_guy.speed(0)
	good_guy.shape("para.gif")
	good_guy.color('blue')
	good_guy.penup()
	good_guy.goto(0,250)
	good_guy.speed = random.randint(1,4)
	good_guys.append(good_guy)



# Made the pen for score and lives
pen = turtle.Turtle()
pen.hideturtle()
pen.speed(0)
pen.shape('square')
pen.color('white')
pen.penup()
pen.goto(0, 260)
font = ('Courier', 24, 'normal')
#pen.write("Score: {} Lives: {}".format(score, lives), align='center', font=font)

# Function
def go_left():
	player.direction = 'left'

def go_right():
	player.direction = 'right'

# Keyborad Binding
wn.listen()
wn.onkeypress(go_left, 'Left')
wn.onkeypress(go_right, 'Right')


# Main game loop
while True:
	# Update screen
	wn.update()

	# move the player
	if player.direction == 'left':
		x = player.xcor()
		x -=3
		player.setx(x)

	if player.direction == 'right':
		x = player.xcor()
		x +=3
		player.setx(x)

	# Move the good guy
	for good_guy in good_guys:
		y = good_guy.ycor()
		y -= good_guy.speed
		good_guy.sety(y)

		# Check if off the screen
		if y< -300:
			#good_guy.goto(0,250)
			x = random.randint(-380, 380)
			y = random.randint(300, 400)
			good_guy.goto(x,y)

		# Check for a collision with the player
		if good_guy.distance(player)<20:
			#print ("COLLISION")
			x = random.randint(-380, 380)
			y = random.randint(300, 400)
			good_guy.goto(x,y)
			score +=10
			lives =1
			pen.clear()
			pen.write("Score: {} Lives: {}".format(score, lives), align='center', font=font)
		
turtle.mainloop()











