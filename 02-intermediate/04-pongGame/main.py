# Create the screen
# Create and move paddle
# Create another paddle
# TODO: Create ball and make it move
# TODO: Detect collision with wall and bounce
# TODO: Detect collistion with paddle
# TODO: Detect when paddle misses
# TODO: Keep score

from turtle import Screen
from paddle import Paddle

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("My Pong Game")
screen.tracer(0)


paddle_R = Paddle((350, 0))
paddle_L = Paddle((-350, 0))


# event listeners to detect key strokes
screen.listen()
screen.onkey(paddle_L.go_up, "w")
screen.onkey(paddle_L.go_down, "s")
screen.onkey(paddle_R.go_up, "Up")
screen.onkey(paddle_R.go_down, "Down")

game_is_on = True
while game_is_on:
    screen.update()


screen.exitonclick()
