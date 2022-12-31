from turtle import Turtle
from random import choice as ch, randint
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self):
        self.all_cars = []

    def create_car(self):
        new_car = Turtle(shape="square")
        new_car.penup()
        new_car.shapesize(stretch_len=1, stretch_wid=2)
        new_car.color(ch(COLORS))
        random_y = randint(-250, 250)
        new_car.goto(300, random_y)
        self.all_cars.append(new_car)
