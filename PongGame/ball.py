from turtle import  Turtle


class Ball(Turtle):
    def __init__(self, x: float, y: float):
        super.__init__()
        self.goto(x, y)
        # self.shapesize(stretch_wid=5, stretch_len=1)
        self.shape("circle")
        self.color("green")
        self.penup()
