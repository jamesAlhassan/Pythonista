from turtle import Turtle, Screen
from random import choice as ch


is_race_on = False
colors =["red", "orange", "yellow", "blue", "green", "purple"]
y_positions = [0, 30, 60, 90, -30, -60]
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput("Make your bet", prompt="Who's going to win this turtle race? Enter a color: ")
all_turtles = []

for timmy in range(len(colors)):
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.color(colors[timmy])
    new_turtle.goto(x=-235, y=y_positions[timmy])
    all_turtles.append(new_turtle)


if user_bet:
    is_race_on = True



screen.listen()

screen.exitonclick()