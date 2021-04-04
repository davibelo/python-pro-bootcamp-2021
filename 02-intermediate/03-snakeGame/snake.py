from turtle import Screen, Turtle
import time

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20

class Snake:
    """ Creates and control a snake """

    def __init__(self):
        self.segments = []
        self.create_snake()

    def create_snake(self):
        """create a snake with 3 segments"""

        for position in STARTING_POSITIONS:
            new_segment = Turtle()
            new_segment.shape("square")
            new_segment.color("white")
            new_segment.penup()
            new_segment.goto(position)
            self.segments.append(new_segment)

    def move(self):
        """moves the snake"""
        for seg in range(len(self.segments) - 1, 0, -1):
            # position of the previous segment
            new_x = self.segments[seg - 1].xcor()
            new_y = self.segments[seg - 1].ycor()
            # segment go to previous segment position
            self.segments[seg].goto(new_x, new_y)
        self.segments[0].forward(MOVE_DISTANCE)