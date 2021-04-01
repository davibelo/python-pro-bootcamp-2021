from turtle import Turtle, Screen

tim = Turtle()

tim.shape("turtle")
tim.color("#457b9d")

for _ in range(4):
    tim.forward(100)
    tim.right(90)

screen = Screen()
screen.exitonclick()

