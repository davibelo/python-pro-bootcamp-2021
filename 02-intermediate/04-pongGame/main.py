# Create the screen
# Create and move paddle
# Create another paddle
# Create ball and make it move
# Detect collision with wall and bounce
# Detect collistion with paddle
# TODO: Detect when paddle misses
# TODO: Keep score

from turtle import Screen
from paddle import Paddle
from ball import Ball
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("My Pong Game")
screen.tracer(0)


paddle_R = Paddle((350, 0))
paddle_L = Paddle((-350, 0))
ball = Ball()


# event listeners to detect key strokes
screen.listen()
screen.onkey(paddle_L.go_up, "w")
screen.onkey(paddle_L.go_down, "s")
screen.onkey(paddle_R.go_up, "Up")
screen.onkey(paddle_R.go_down, "Down")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    ball.move()
    print(ball.xcor(),ball.ycor())

    # detect collision with wall and bounce
    if abs(ball.ycor()) > 280:
        ball.bounce_y()      

    # detect collition with right paddle
    if ball.distance(paddle_R) < 50 and ball.xcor() > 320:
        ball.bounce_x()

    # detect collition with left paddle
    if ball.distance(paddle_L) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    

screen.exitonclick()
