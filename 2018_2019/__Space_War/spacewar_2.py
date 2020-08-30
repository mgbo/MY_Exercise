
# SpaceWare by @TokyoEdTech 
# Part III : Getting started
# Game Object / Broder / Boundary Checking

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
			self.lt(60)

		if self.xcor() < -290:
			self.setx(-290)
			self.rt(60)

		if self.ycor() < -290:
			self.sety(-290)
			self.lt(60)

		if self.ycor() > 290:
			#self.setx(290)
			self.rt(60)


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

# Keyboard bindings
turtle.listen()
turtle.onkeypress(player.turn_left,'Left')
turtle.onkeypress(player.turn_right,'Right')
turtle.onkeypress(player.accelerate,'Up')
turtle.onkeypress(player.decelerate,'Down')

# Main game loop
while True:
	#player.fd(player.speed)
	player.move()
	#player.turn_left()





turtle.mainloop()













