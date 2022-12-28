from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Score
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Score()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    #Detect collision with food.
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()

    #Detect collision with wall.
    # if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
    #     game_is_on = False
    #     scoreboard.game_over()

    # show from the other side
    if snake.head.xcor() == 280:
        y = snake.head.ycor()
        snake.head.goto(x=-280, y=y)
    elif snake.head.xcor() == -280:
        y_1 = snake.head.ycor()
        snake.head.goto(x=280, y=y_1)

    if snake.head.ycor() == 280:
        x = snake.head.xcor()
        snake.head.goto(x=x, y=-280)
    elif snake.head.ycor() == -280:
        x_1 = snake.head.xcor()
        snake.head.goto(x=x_1, y=280)


    #Detect collision with tail.
    for segment in snake.segments:
        if segment == snake.head:
            pass
        elif snake.head.distance(segment) < 10:
            game_is_on = False
            scoreboard.game_over()





screen.exitonclick()