from turtle import Turtle
from food import Food


class Score(Food):
    def __init__(self):
        super().__init__()
        self.write(arg="score", align="center")

