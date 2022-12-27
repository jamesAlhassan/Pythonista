from turtle import Turtle
from food import Food


ALIGN = "center"
FONT = ('Cursive', 24, 'normal')


class Score(Food):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.color("green")
        self.goto(0, 265)
        self.write(f"Score: {self.score}", align=ALIGN, font=FONT)
        self.hideturtle()

    def increase_score(self):
        self.score += 1
        self.clear()
        self.write(f"Score: {self.score}", align=ALIGN, font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write(arg="GAME OVER", align=ALIGN, font=FONT)


