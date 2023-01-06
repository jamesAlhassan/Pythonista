import turtle
import pandas as pd

screen = turtle.Screen()
screen.title("US States Game")
image = "regional_map.gif"
screen.addshape(image)

turtle.shape(image)
# df = pd.read_csv("")


def get_mouse_coor(x, y):
    print(x, y)


turtle.onscreenclick(get_mouse_coor)
turtle.mainloop()

answer_state = screen.textinput(title="2020 Election Results", prompt="Enter candidate name or region")
