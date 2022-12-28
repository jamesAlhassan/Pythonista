from turtle import  Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        # self.goto(x, y)
        # self.shapesize(stretch_wid=5, stretch_len=1)
        self.shape("circle")
        self.color("green")
        self.penup()
        self.x_move = 10
        self.y_move = 10

    def ball_move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def ball_bounce(self):
        self.y_move *= -1


