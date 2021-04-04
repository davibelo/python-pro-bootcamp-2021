# TODO: Create a snake body
# TODO: Move the snake
# TODO: Controle the snake
# TODO: Detect collision with food
# TODO: Create a scoreboard
# TODO: Detect collision with a wall
# TODO: Detect collision with itself

from turtle import Screen, Turtle
import time
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

starting_positions = [(0, 0), (-20, 0), (-40, 0)]

segments = []

for position in starting_positions:
    new_segment = Turtle()
    new_segment.shape("square")
    new_segment.color("white")
    new_segment.penup()
    new_segment.goto(position)
    segments.append(new_segment)

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.2)

    for seg_num in range(len(segments)-1, 0, -1):
        # position of the previous segment
        new_x = segments[seg_num - 1].xcor()
        new_y = segments[seg_num - 1].ycor()
        # segment go to previous segment position
        segments[seg_num].goto(new_x, new_y)
    segments[0].forward(20)    
    segments[0].left(90)

screen.exitonclick()
