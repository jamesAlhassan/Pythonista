import turtle
import pandas as pd
from result import Result

details = [(-401, 420), (-399, 387), (-397, 341), (-399, 298), (-403, 256), (-397, 214)]
screen = turtle.Screen()
screen.title("2020 GH Election Results")
image = "regional.gif"
screen.addshape(image)
screen.setup(height=960, width=900)
turtle.shape(image)

result = Result()
all_result = Result()

data = pd.read_csv("presidential_regional_results.csv")
all_party = data['Party'].to_list()
all_candidate = data['Candidate'].to_list()




# def get_mouse_coor(x, y):
#     print(x, y)
#
#
# turtle.onscreenclick(get_mouse_coor)
# turtle.mainloop()

search_party = screen.textinput(title="2020 Election Results", prompt="Enter party")

if search_party in all_party:

    result_data = data[data.Party == search_party]
    result.goto(int(result_data.x), int(result_data.y))
    result.write(f"{result_data.Candidate.item()} \n  {result_data.Party.item()} \n {result_data.Votes.item()}", font=("Courier", 16, "normal"))
    a = 0
    for detail in details:
        all_result.goto(detail)
        all_result.write(f"{all_candidate[a]}")
        a += 1




screen.exitonclick()