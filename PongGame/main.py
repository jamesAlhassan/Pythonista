from turtle import Screen, Turtle
# Screen Setup
screen = Screen()
screen.setup(width=800, height=600)
screen.title("Ping Pong")
screen.bgcolor("black")
screen.tracer(0)


paddle = Turtle(shape="square")
paddle.shapesize(stretch_wid=5, stretch_len=1)
paddle.color("white")
paddle.penup()
paddle.goto(x=350, y=0)

def move_up():
    new_y = paddle.ycor() + 20
    paddle.goto(paddle.xcor(), new_y)

def move_down():
    new_y = paddle.ycor() - 20
    paddle.goto(paddle.xcor(), new_y)


screen.listen()
screen.onkey(move_up, "Up")
screen.onkey(move_down, "Down")

game_is_on = True
while game_is_on:
    screen.update()
screen.exitonclick()