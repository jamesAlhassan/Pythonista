import time
from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
# Screen Setup
screen = Screen()
screen.setup(width=800, height=600)
screen.title("Ping Pong")
screen.bgcolor("black")
screen.tracer(0)

# Paddles
left_paddle = Paddle(350, 0)
right_paddle = Paddle(-350, 0)

#  Ball
ball = Ball()


screen.listen()
screen.onkey(left_paddle.move_up, "Up")
screen.onkey(left_paddle.move_down, "Down")
screen.onkey(right_paddle.move_up, "w")
screen.onkey(right_paddle.move_down, "s")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    ball.ball_moving()


screen.exitonclick()