from turtle import Turtle
import random

class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("circle")
        self.color("blue")
        self.shapesize(stretch_wid=1, stretch_len=1)
        self.speed("fastest")
        self.refresh()        

    def refresh(self):
        random_x = random.choice(range(-200, 200, 20))
        random_y = random.choice(range(-200, 200, 20))
        self.goto(random_x, random_y)
