from turtle import Turtle
import  pandas as pd

class Result(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color("green")