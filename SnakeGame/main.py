from snake

# Snake movement
game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.1)

    for sn in range(len(snakes) - 1, 0, -1):
        new_x = snakes[sn - 1].xcor()
        new_y = snakes[sn - 1].ycor()
        snakes[sn].goto(x=new_x, y=new_y)
    snakes[0].fd(20)
    snakes[0].lt(90)



screen.exitonclick()