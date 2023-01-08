import turtle
import pandas as pd
from result import Result

details = [(-401, 420), (-401, 387), (-401, 341), (-401, 298), (-401, 256), (-401, 214), (220, 425), (220, 381),
           (220, 302), (220, 250), (220, 185), (220, 103)]

screen = turtle.Screen()
screen.title("2020 GH Election Results")
image = "regional.gif"
screen.addshape(image)
screen.setup(height=960, width=900)
turtle.shape(image)

result = Result()
all_result = Result()
heading = Result()

data = pd.read_csv("presidential_regional_results.csv")
all_party = data['Party'].to_list()
all_candidate = data['Candidate'].to_list()
all_votes = data['Votes'].to_list()
all_region = data['Region'].to_list()
print(all_region)



# def get_mouse_coor(x, y):
#     print(x, y)
#
#
# turtle.onscreenclick(get_mouse_coor)
# turtle.mainloop()
#
search_party = screen.textinput(title="2020 Election Results", prompt="Enter Party").upper()
search_region = screen.textinput(title="2020 Election Results", prompt="Enter Region").capitalize()

if search_party in all_party and search_region in all_region:
    heading.color('black')
    heading.goto(-115, 459)
    heading.write(f"{search_region} Regional Details")

    result_data = data[data.Party == search_party]
    result_data1 = data[data.Region == search_region]
    result.color("red")
    result.goto(int(result_data.x), int(result_data.y))
    result.write(f"{result_data.Candidate.item()} \n  {result_data.Party.item()} \n {result_data1.Votes.item()}", font=("Courier", 16, "bold"))

    a = 0
    for detail in details:
        all_result.color('green')
        all_result.goto(detail)
        all_result.write(f"{all_candidate[a]} \n {all_votes[a]}")
        a += 1




screen.exitonclick()