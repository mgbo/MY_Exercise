
# Space Invaders
# set up the screen

import turtle
import os
import math
import random

# Set up the screen
wn = turtle.Screen()
wn.bgcolor("black")
wn.title("Space Invaders")
wn.bgpic('alien1.gif')
wn.tracer(0)

wn.register_shape('jet.gif')
wn.register_shape('jet1.gif')

# Draw Border
border_pen = turtle.Turtle()
border_pen.speed(0)
border_pen.color('white')
border_pen.penup()
border_pen.setposition(-300,-300)
border_pen.pendown()
border_pen.pensize(3)

for side in range(4): # для рамки
	border_pen.fd(600)
	border_pen.lt(90)

border_pen.hideturtle()

# Set the score to 0
score = 0
lives = 3

# Draw the score
score_pen = turtle.Turtle()
score_pen.speed(0)
score_pen.color('white')
score_pen.penup()
score_pen.setposition(-290, 280)
fb = ('Arial', 20, 'normal')
score_pen.write('Score: {} lives: {}'.format(score, lives), align='left', font=fb)
score_pen.hideturtle()

# Create the player turtle
player = turtle.Turtle()
player.color("blue")
player.shape("jet.gif")
player.penup()
player.speed(0)
player.setposition(0,-250)
player.setheading(90)

playerspeed = 15

# Choose a number of enemies
number_of_enemies = 10

# Create an empty list of enemies
enemies = []

for _ in range(number_of_enemies):
	# Create the enemy
	enemy = turtle.Turtle()
	enemy.color('red')
	enemy.shape('jet1.gif')
	enemy.penup()
	enemy.speed(0)
	x = random.randint(-200, 200)
	y = random.randint(100, 250)
	enemy.setposition(x,y) 

	enemies.append(enemy) # Add enemy to the list of enemies

enemyspeed = 1

# Create the player's bullet
bullet = turtle.Turtle()
bullet.color("yellow")
bullet.shape('triangle')
bullet.shapesize(0.5, 0.5)
bullet.penup()
bullet.setheading(90)
bullet.hideturtle()

bulletspeed = 20

# Deine bullet state
#ready - ready to fire
#fire - buleet is firing
bulletstate = 'ready'


# Move the player left and right
def move_left():
	x = player.xcor()
	x -= playerspeed

	if x < -280:
		x = -280
	player.setx(x)

def move_right():
	x = player.xcor()
	x +=playerspeed

	if x > 280:
		x = 280

	player.setx(x)

# fire bullet
def fire_bullet():

	# Declare bulletstate as a global if it needs changed
	global bulletstate

	if  bulletstate == 'ready':

		bulletstate = 'fire'
		# Move the bullet to the just above the player
		x = player.xcor()
		y = player.ycor() + 10
		bullet.setposition(x,y)
		bullet.showturtle()

def isCollision(t1, t2):
	distance = math.sqrt(math.pow(t1.xcor() - t2.xcor(),2) + math.pow(t1.ycor() - t2.ycor(),2))

	if distance < 15:
		return True
	else:
		return False


# Create keyboard bindings
turtle.listen()
turtle.onkeypress(move_left,"Left")
turtle.onkeypress(move_right,"Right")
turtle.onkeypress(fire_bullet, "space")

# Main game loop
while True:
	wn.update()

	# Move the enemy
	
	for enemy in enemies:
		x = enemy.xcor()
		x += enemyspeed
		enemy.setx(x)

		# Move the enemy back and down
		if enemy.xcor() > 280:
			y = enemy.ycor()
			y -=40
			enemyspeed *= -1
			enemy.sety(y)


		if enemy.xcor() < -280:
			y = enemy.ycor()
			y -=40
			enemyspeed *= -1
			enemy.sety(y)

		# Check to see if the bullet has gone to the top
		if bullet.ycor() > 275:
			bullet.hideturtle()
			bulletstate = 'ready'

		# Check for a collision between the bullet and the enemy
		if isCollision(bullet, enemy):
			# Reset the bullet 
			bullet.hideturtle()
			bulletstate = "ready"
			bullet.setposition(0,-400)

			#Reset the enemy
			#enemy.setposition(-200, 250)
			x = random.randint(-200, 200)
			y = random.randint(100, 250)
			enemy.setposition(x, y)

			score +=1
			score_pen.clear()
			fb = ('Arial', 20, 'normal')
			score_pen.write('Score: {} lives: {}'.format(score, lives), align='left', font=fb)


		if isCollision(player, enemy):
			player.hideturtle()
			enemy.hideturtle()
			lives -=1
			if lives<0:
				print ("Game Over")
				fb = ('Arial', 20, 'normal')
				score_pen.write('Score: {} lives: {}'.format(score, lives), align='left', font=fb)
				break

	# Move th bullet
	y = bullet.ycor()
	y += bulletspeed
	bullet.sety(y)






turtle.done()

turtle.exitonclick()












