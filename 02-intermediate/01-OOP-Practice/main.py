# External module contains classes

# importing turtle module and using Turtle class
# import turtle
# timmy = turtle.Turtle()  

# importing only specific classes from turtle module
import tkinter
from turtle import Turtle, Screen

# turtle graphics documentation
# https://docs.python.org/3/library/turtle.html

jimmy = Turtle()
# see the object assigned to a computer memory
print(jimmy)

jimmy.shape("turtle")

my_screen = Screen()
# print(my_screen.canvheight)

my_screen.exitonclick()

