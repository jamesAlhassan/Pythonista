import time
from turtle import Turtle, Screen

# screen Setup
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

# Turtle Setup
snakes = []
pos = [0, -20, -40]
for x in range(len(pos)):
    snake = Turtle(shape="square")
    snake.color("white")
    snake.penup()
    snake.goto(x=pos[x], y=0)
    snakes.append(snake)


game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.1)
    for sn in snakes:
        sn.fd(20)







screen.exitonclick()