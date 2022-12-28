from turtle import Screen, Turtle
from paddle import Paddle
# Screen Setup
screen = Screen()
screen.setup(width=800, height=600)
screen.title("Ping Pong")
screen.bgcolor("black")
screen.tracer(0)


left_paddle = Paddle(350, 0)
right_paddle = Paddle(-350, 0)
def move_up():
    new_y = paddle.ycor() + 20
    paddle.goto(paddle.xcor(), new_y)




screen.listen()
screen.onkey(move_up, "Up")
screen.onkey(move_down, "Down")

game_is_on = True
while game_is_on:
    screen.update()
screen.exitonclick()