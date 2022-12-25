from turtle import Turtle, Screen

# screen Setup
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")

# Turtle Setup
pos = [0, -20, -40]
for x in range(len(pos)):
    turtle = Turtle(shape="square")
    turtle.color("white")
    turtle.goto(x=pos[x], y=0)







screen.exitonclick()