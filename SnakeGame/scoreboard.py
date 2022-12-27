from turtle import Turtle
from food import Food


class Score(Food):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.color("green")
        self.goto(0, 265)
        self.write(f"Score: {self.score}", align="center", font=('Arial', 24, 'normal'))
        self.hideturtle()

    def increase_score(self):
        self.score += 1
        self.clear()
        self.write(f"Score: {self.score}", align="center", font=('Arial', 24, 'normal'))


