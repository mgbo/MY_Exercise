
def main():
    window = turtle.Screen()  # creat a screen
    window.bgcolor("blue")
    lucy = turtle.Turtle()
    lucy.shape("turtle")
    lucy.color("red")
    lucy.width(5)
    lucy.speed(0)

    # Drawing flower
    flower(lucy, 10, 40, 100, 360)

    # Drawing pedicel
    lucy.color("brown")
    lucy.rt(90)
    lucy.fd(200)

    # Drawing leaf
    lucy.rt(270)
    lucy.color("green")
    leaf(lucy, 40, 80, 180)
    lucy.ht()
    window.exitonclick()

if __name__ == "__main__":
    