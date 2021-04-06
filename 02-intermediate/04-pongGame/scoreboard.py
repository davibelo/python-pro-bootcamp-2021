from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 18, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.goto(0, 270)
        self.color("white")
        self.score_L = 0
        self.score_R = 0
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(f"Score: {self.score_L}/{self.score_R}",
                   align=ALIGNMENT, font=FONT)

    def increase_score_L(self):
        self.score_L += 1
        self.clear()
        self.update_scoreboard()

    def increase_score_R(self):
        self.score_R += 1
        self.clear()
        self.update_scoreboard()

    def game_over(self):
        self.goto(0, 0)
        if self.score_L > self.score_R:
            winner = "Player 1"
        else:
            winner = "Player 2"
        self.write(f"{winner} wins!",
                   align=ALIGNMENT, font=FONT)
        
