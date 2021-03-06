# create turtle player that moves up
# create random generated cars that moves right to left
# detect turtle colliding with cars
# detect when turtle reaches top and makes game to level up
# creates a scoreboard to keep track of level

import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()

screen.listen()
screen.onkeypress(player.move_up,"Up")
screen.onkeypress(player.move_down, "Down")

car_manager = CarManager()
scoreboard = Scoreboard()

game_is_on = True
while game_is_on:
    time.sleep(0.05)
    screen.update()
    car_manager.create_car()
    car_manager.move_cars()

    # detect collision with cars
    for car in car_manager.cars:
        if car.distance(player) < 20:
            game_is_on = False
            scoreboard.game_over()        

    # detect turtle reaching top
    if player.is_on_top():
        player.go_to_start()
        car_manager.level_up()
        scoreboard.level_up()
        
screen.exitonclick()
