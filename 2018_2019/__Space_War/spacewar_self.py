
# SpaceWare by @TokyoEdTech 
# Part I : Getting started

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

class Bullet(Sprite):
	def __init__(self, spriteshape, color, startx, starty):
		Sprite.__init__(self, spriteshape, color, startx, starty)
		self.speed = 15
		self.shapesize(0.5, 0.5)
		self.setpos(startx,starty)
		self.showturtle()

# Create my sprites
player = Player('triangle','white', 0, 0)

b = Bullet('circle', 'red', player.xcor(), player.ycor()+10)

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













