from turtle import  Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        # self.goto(x, y)
        # self.shapesize(stretch_wid=5, stretch_len=1)
        self.shape("circle")
        self.color("green")
        self.penup()

    def ball_moving(self):
        new_x = self.xcor() + 10
        new_y = self.ycor() + 10
        self.goto(new_x, new_y)

