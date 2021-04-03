import turtle as t
import random
import colorgram

# getting colors from painting
colors = colorgram.extract(
    "/home/davibelo/Desktop/python-pro-bootcamp-2021/02-intermediate/02-turtle_and_GUI/image.jpg", 30)

rgb_colors = []
for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    rgb_colors.append((r, g, b))

first_color = rgb_colors[0]
colors = rgb_colors[4:]

# setting colormode to rgb
t.colormode(255)

# setting turtle
tim = t.Turtle()
tim.shape("classic")
tim.speed(10)
tim.pensize(1)

# setting screen
width = 1500
height = 800
screen = t.Screen()
screen.setup(width, height)
screen.bgcolor(first_color)

# making the painting
x = -200
y = -300
for _ in range(10):
    tim.penup()
    tim.goto(x, y)
    for _ in range(10):
        tim.pendown()
        tim.color(random.choice(colors))
        tim.dot(15)
        tim.penup()
        tim.forward(50)
    y += 50    
tim.hideturtle()

# setting screen to exit on click
screen.exitonclick()
