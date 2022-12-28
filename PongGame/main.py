from turtle import Screen, Turtle
# Screen Setup
screen = Screen()
screen.setup(width=800, height=600)
screen.title("Ping Pong")
screen.bgcolor("black")



paddle = Turtle(shape="square")
paddle.shapesize(stretch_wid=5, stretch_len=1)
paddle.color("white")
paddle.penup()
paddle.goto(x=350, y=0)


screen.exitonclick()