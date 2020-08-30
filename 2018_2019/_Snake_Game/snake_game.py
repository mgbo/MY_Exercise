
'''
Simple Snake Game in python3 for Beginners
Part 1: Getting Started
'''
import turtle

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



# Main game loop
while  True:
	wn.update()

turtle.mainloop()





