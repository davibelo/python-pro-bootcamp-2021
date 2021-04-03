import turtle as t
import random

tim = t.Turtle()
t.colormode(255)
tim.speed("fastest")

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


def draw_spirograph(size_of_gap):
    for _ in range(int(360 / size_of_gap)):
        tim.color(random_color())
        tim.circle(100)
        tim.setheading(tim.heading() + size_of_gap)


draw_spirograph(10)

# setting screen to exit on click
screen.exitonclick()
