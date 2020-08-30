import turtle
import random

# setup the window with a background colour
wn = turtle.Screen()
wn.bgcolor("cyan")

# assign a name to your turtle
elsa = turtle.Turtle()
elsa.speed(0)

# create a list of colours
sfcolor = ["white", "blue", "purple", "grey", "magenta"]

# create a function to create different size snowflakes
def snowflake(size):
# move the pen into starting position
    elsa.penup()
    elsa.forward(10*size)
    elsa.left(45)
    elsa.pendown()
    elsa.color(random.choice(sfcolor))
    # draw branch 8 times to make a snowflake
    for i in range(8):
        branch(size)   
        elsa.left(45)
    
def branch(size):
    for i in range(3):
        for i in range(3):
            elsa.forward(10.0*size/3)
            elsa.backward(10.0*size/3)
            elsa.right(45)
        elsa.left(90)
        elsa.backward(10.0*size/3)
        elsa.left(45)
    elsa.right(90) 
    elsa.forward(10.0*size)
branch(5)
wn.exitonclick()  