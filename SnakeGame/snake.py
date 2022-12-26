from turtle import Turtle


X_POSITIONS = [0, -20, -40]
MOVE_DISTANCE = 20


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
            snake.goto(x=X_POSITIONS[x], y=0)
            self.snakes.append(snake)

    def move_snake(self):
        for sn in range(len(self.snakes) - 1, 0, -1):
            new_x = self.snakes[sn - 1].xcor()
            new_y = self.snakes[sn - 1].ycor()
            self.snakes[sn].goto(x=new_x, y=new_y)
        self.head.fd(MOVE_DISTANCE)

    def up(self):
        self.head.setheading(90)

    def down(self):
        self.head.setheading(270)

    def left(self):
        self.head.setheading(180)

    def right(self):
        self.head.setheading(0)




