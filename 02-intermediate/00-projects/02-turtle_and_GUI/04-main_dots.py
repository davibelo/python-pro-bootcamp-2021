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
tim.speed("fastest")
tim.pensize(1)

# setting screen
width = 1500
height = 800
screen = t.Screen()
screen.setup(width, height)
screen.bgcolor(first_color)

# making the painting
painting_size = 10
dots_distance = 50
x = -200
y = -300
for _ in range(painting_size):
    tim.penup()
    tim.goto(x, y)
    for _ in range(painting_size):        
        tim.color(random.choice(colors))
        tim.dot(15)        
        tim.forward(dots_distance)
    y += dots_distance    
tim.hideturtle()

# setting screen to exit on click
screen.exitonclick()
