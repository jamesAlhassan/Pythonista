from turtle import Turtle


X_POSITIONS = [0, -20, -40]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self):
        self.snakes = []
        self.create_snake()
        self.head = self.snakes[0]

    def create_snake(self):
        for x in range(len(X_POSITIONS)):
            snake = Turtle(shape="square")
            snake.color("white")
            snake.penup()
            # snake.shapesize(stretch_wid=0.7, stretch_len=0.7)
            snake.goto(x=X_POSITIONS[x], y=0)
            self.snakes.append(snake)

    def move_snake(self):
        for sn in range(len(self.snakes) - 1, 0, -1):
            new_x = self.snakes[sn - 1].xcor()
            new_y = self.snakes[sn - 1].ycor()
            self.snakes[sn].goto(x=new_x, y=new_y)
        self.head.fd(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)




