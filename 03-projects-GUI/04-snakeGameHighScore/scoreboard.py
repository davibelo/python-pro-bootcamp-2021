from turtle import Turtle
import os

ALIGNMENT = "center"
FONT = ("Courier", 18, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.goto(0, 270)
        self.color("white")
        self.hideturtle()
        self.score = 0
        self.high_score = 0
        self.read_high_score_file()
        self.update_scoreboard()

    def read_high_score_file(self):
        script_dir = os.path.dirname(__file__)
        rel_path = "data.txt"
        abs_file_path = os.path.join(script_dir, rel_path)
        with open(abs_file_path) as file:
            self.high_score = int(file.read())

    def write_high_score_file(self, high_score):
        script_dir = os.path.dirname(__file__)
        rel_path = "data.txt"
        abs_file_path = os.path.join(script_dir, rel_path)
        with open(abs_file_path, mode="w") as file:
            file.write(str(high_score))

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} HighScore: {self.high_score}",
                   align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
        self.write_high_score_file(self.high_score)
        self.score = 0
        self.update_scoreboard()
