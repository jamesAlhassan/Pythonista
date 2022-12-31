import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard


# Screen Setup
screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

# Object instantiation
player = Player()
car_manager = CarManager()


screen.listen()
screen.onkey(player.go_up, "Up")

game_is_on = True
while game_is_on:
    # updated every 0.1 secs
    time.sleep(0.1)
    screen.update()

    car_manager.create_car()
    car_manager.move_cars()

    #     Detect car Collision
    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            game_is_on = False

    # crosses all the cars
    if player.is_at_finish():
        player.go_to_start()
screen.exitonclick()