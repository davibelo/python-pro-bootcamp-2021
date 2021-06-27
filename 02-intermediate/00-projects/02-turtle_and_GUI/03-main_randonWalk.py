import turtle as t
import random

tim = t.Turtle()
t.colormode(255)

# setting screen size
width = 1500
height = 800
screen = t.Screen()
screen.setup(width, height)


def random_color():
    """returns a tuple with r,g,b values"""
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r, g, b)


# setting properties
tim.shape("circle")
tim.speed("fastest")
tim.pensize(15)

# setting start position
tim.penup()
tim.setposition(0, 0)
tim.pendown()


# setting the number of walks
n = 300

directions = [0, 90, 180, 270]
# directions = [0, 45, 90, 135, 180, 225, 270, 315, 360]

# drawing a random walk
for i in range(n):
    tim.setheading(random.choice(directions))
    tim.color(random_color())
    tim.forward(25)


# setting screen to exit on click
screen.exitonclick()
