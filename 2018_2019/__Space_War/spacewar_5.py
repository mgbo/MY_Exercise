
# SpaceWare by @TokyoEdTech 
# Part III : Getting started
# Game Object / Broder / Boundary Checking
# Create enemy and collision
# Create a Missile
# Create an Ally


import os
import random
import turtle


turtle.speed(0) # Set the animations sepeed to the maximum
turtle.bgcolor('black') # Change the background color
turtle.hideturtle() # hide the default turtle
turtle.setundobuffer(1) # This saves memory
turtle.tracer(1) # This speeds up drawing

turtle.register_shape('fishtank.gif')

class Sprite(turtle.Turtle):
	def __init__(self, spriteshape, color, startx, starty):
		turtle.Turtle.__init__(self, shape= spriteshape)
		#self.shape(spriteshape)
		self.speed(0)
		self.penup()
		self.color(color)
		self.goto(startx, starty)
		self.speed = 1

	def move(self):
		self.fd(self.speed)

		# Boundary detection
		if self.xcor() > 290:
			self.setx(290)
			self.rt(60)

		if self.xcor() < -290:
			self.setx(-290)
			self.rt(60)

		if self.ycor() > 290:
			self.sety(290)
			self.rt(60)

		if self.ycor() < -290:
			self.sety(290)
			self.rt(60)

	def is_collision(self, other):
		if (self.xcor() >= (other.xcor() - 20)) and \
		(self.xcor() <= (other.xcor() + 20)) and \
		(self.ycor() >= (other.ycor() - 20)) and \
		(self.ycor() <= (other.ycor() + 20)):
			return True
		else:
			return False



class Player(Sprite):
	def __init__(self, spriteshape, color, startx, starty):
		Sprite.__init__(self, spriteshape, color, startx, starty)
		self.speed = 2
		self.lives = 3

	def turn_left(self):
		self.lt(45)

	def turn_right(self):
		self.rt(45)

	def accelerate(self):
		self.speed +=1

	def decelerate(self):
		self.speed -=1

class Enemy(Sprite):
	def __init__(self, spriteshape, color, startx, starty):
		Sprite.__init__(self, spriteshape, color, startx, starty)
		self.speed = 6
		self.setheading(random.randint(0, 360))

class Ally(Sprite):
	def __init__(self, spriteshape, color, startx, starty):
		Sprite.__init__(self, spriteshape, color, startx, starty)
		self.speed = 8
		self.shapesize(0.5, 0.5)
		self.setheading(random.randint(0, 360))

class Missile(Sprite):
	def __init__(self, spriteshape, color, startx, starty):
		Sprite.__init__(self, spriteshape, color, startx, starty)
		self.shapesize(0.3, 0.3)
		self.speed = 20
		self.status = 'ready'
		#self.goto(-300, 300)

	def fire(self):
		if self.status == 'ready':
			self.goto(player.xcor(), player.ycor())
			self.setheading(player.heading())
			self.status = 'firing'

	def move(self):
		if self.status == 'ready':
			self.goto(-1000, 1000)

		if self.status == 'firing':
			self.fd(self.speed)

		# Border check
		if self.xcor() < -290 or self.xcor() > 290 or \
		self.ycor() < -290 or self.ycor() > 290:
			self.goto(-1000, 1000)
			self.status = 'ready'

class Game():
	def __init__(self):
		self.level = 1
		self.score = 0
		self.state = 'playing'
		self.pen = turtle.Turtle()
		self.lives = 3

	def draw_border(self):
		# Draw border
		self.pen.penup()
		self.pen.speed(0)
		self.pen.color('white')
		self.pen.pensize(3)
		self.pen.goto(-300, 300)
		self.pen.pendown()

		for side in range(4):
			self.pen.fd(600)
			self.pen.rt(90)

		self.pen.penup()
		self.pen.ht()

# Crate Game object
game = Game()
game.draw_border() # Draw the broder

# Create my sprites
player = Player('turtle','white', 0, 0)
enemy = Enemy("circle", 'blue', -100, 0)
missile = Missile('triangle', 'red', 0, 0)
ally = Ally('square', 'yellow', 0, 0)

# Keyboard bindings
turtle.listen()
turtle.onkeypress(player.turn_left,'Left')
turtle.onkeypress(player.turn_right,'Right')
turtle.onkeypress(player.accelerate,'Up')
turtle.onkeypress(player.decelerate,'Down')
turtle.onkeypress(missile.fire, 'space')

# Main game loop
while True:
	#player.fd(player.speed)

	player.move()
	enemy.move()
	missile.move()
	ally.move()

	# Check for a collision
	if player.is_collision(enemy):
		x = random.randint(-250, 250)
		y = random.randint(-250, 250)
		enemy.goto(x,y)

	# Check for a collision between the missile and the enemy
	if missile.is_collision(enemy):
		x = random.randint(-250, 250)
		y = random.randint(-250, 250)
		enemy.goto(x,y)

	# Check for a collision between the missile and the enemy
	if missile.is_collision(ally):
		x = random.randint(-250, 250)
		y = random.randint(-250, 250)
		enemy.goto(x,y)







turtle.mainloop()













