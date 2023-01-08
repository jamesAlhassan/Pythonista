import turtle
import pandas as pd

screen = turtle.Screen()
screen.title("2020 GH Election Results")
image = "regional.gif"
screen.addshape(image)
screen.setup(height=960, width=900)
turtle.shape(image)

data = pd.read_csv("presidential_regional_results.csv")
all_party = data['Party'].to_list()




# def get_mouse_coor(x, y):
#     print(x, y)
#
#
# turtle.onscreenclick(get_mouse_coor)
# turtle.mainloop()

search_party = screen.textinput(title="2020 Election Results", prompt="Enter party")

if search_party in all_party:
    result = turtle.Turtle()
    result.hideturtle()
    result.penup()
    result_data = data[data.Party == search_party]
    result.goto(int(result_data.x), int(result_data.y))
    result.write(f"{result_data.Candidate.item()} \n  {result_data.Party.item()} \n {result_data.Votes.item()}")

    print(result_data)





screen.exitonclick()