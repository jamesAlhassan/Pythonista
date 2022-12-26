from turtle import Turtle, Screen
import time

X_POSITIONS = [0, -20, -40]
class Snake:
# screen Setup
    def __init__(self):
        self.snakes = []
        self.create_snake()

    def create_snake(self):
        for x in range(len(X_POSITIONS)):
            snake = Turtle(shape="square")
            snake.color("white")
            snake.penup()
            snake.goto(x=X_POSITIONS[x], y=0)
            self.snakes.append(snake)
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)


# Turtle Setup


