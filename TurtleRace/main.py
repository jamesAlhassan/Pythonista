from turtle import Turtle, Screen
from random import choice as ch

colors =["red", "orange", "yellow", "blue", "green", "purple"]
y_positions = [0, 30, 60, 90, -30, -60]
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput("Make your bet", prompt="Who's going to win this turtle race? Enter a color: ")

for timmy in range(len(colors)):
    tim = Turtle(shape="turtle")
    tim.penup()
    tim.color(colors[timmy])
    tim.goto(x=-235, y=y_positions[timmy])



screen.listen()

screen.exitonclick()