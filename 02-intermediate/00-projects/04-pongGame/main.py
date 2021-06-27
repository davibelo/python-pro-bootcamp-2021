# Create the screen
# Create and move paddle
# Create another paddle
# Create ball and make it move
# Detect collision with wall and bounce
# Detect collistion with paddle
# Detect when paddle misses
# Keep score

from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("My Pong Game")
screen.tracer(0)

paddle_R = Paddle((350, 0))
paddle_L = Paddle((-350, 0))
ball = Ball()
scoreboard = Scoreboard()

# event listeners to detect key strokes
screen.listen()
screen.onkeypress(paddle_L.go_up, "w")
screen.onkeypress(paddle_L.go_down, "s")
screen.onkeypress(paddle_R.go_up, "Up")
screen.onkeypress(paddle_R.go_down, "Down")

game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # detect collision with wall and bounce
    if abs(ball.ycor()) > 280:
        ball.bounce_y()

    # detect collition with right paddle
    if ball.distance(paddle_R) < 50 and ball.xcor() > 320:
        ball.bounce_x()

    # detect collition with left paddle
    if ball.distance(paddle_L) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    # for improving precision of bounce when hit paddles (hotfix)
    if -10 < ball.xcor() < 10 :
        ball.reset_paddle_hit()

    # detect when right paddle misses
    if ball.xcor() > 400:
        scoreboard.increase_score_L()
        ball.reset_position()

    # detect when left paddle misses
    if ball.xcor() < -400:
        scoreboard.increase_score_R()
        ball.reset_position()

    # game over
    if scoreboard.score_L > 2 or scoreboard.score_R > 2:
        scoreboard.game_over()
        game_is_on = False

screen.exitonclick()
