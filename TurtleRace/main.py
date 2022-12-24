from turtle import Turtle, Screen
from random import choice as ch

colors =["red", "orange", "yellow", "blue", "green", "purple"]
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput("Make your bet", prompt="Who's going to win this turtle race? Enter a color: ")


reddy = Turtle(shape="turtle")
reddy.penup()
reddy.color("red")
reddy.goto(x=-235, y=0)

orangy = Turtle(shape="turtle")
orangy.penup()
orangy.color("orange")
orangy.goto(x=-235, y=30)

yellowy = Turtle(shape="turtle")
yellowy.penup()
yellowy.color("yellow")
yellowy.goto(x=-235, y=30)

screen.listen()

screen.exitonclick()