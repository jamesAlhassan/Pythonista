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

data = pd.read_csv("presidential_regional_results.csv", index_col="Region")
# print(data)


# def get_mouse_coor(x, y):
#     print(x, y)
#
#
# turtle.onscreenclick(get_mouse_coor)
# turtle.mainloop()

# search_party = screen.textinput(title="2020 Election Results", prompt="""Enter Party:
# 0=NPP,
# 1=NDC,
# 2=GUM",
# 3=CPP,
# 4=GFP,
# 5=GCPP,
# 6=APC,
# 7=LPG,
# 8=PNC,
# 9=PPP
#
# """)
# search_region = screen.textinput(title="2020 Election Results", prompt="""Enter Region:
# 0=AHAFO,
# 1=ASHANTI,
# 2=BONO",
# 3=BONO EAST,
# 4=CENTRAL,
# 5=EASTERN,
# 6=GREATER ACCRA,
# 7=NORTH EAST,
# 8=NORTHERN,
# 9=OTI
# """)
search_party = screen.textinput(title="2020 Election Results", prompt="Enter Party: ").upper()
search_region = screen.textinput(title="2020 Election Results", prompt=" Enter Region: ").capitalize()
for index, details in data.iterrows():
    if search_region == index and search_party == details.Party:
        print(f'{details.Candidate} had {details.Votes} in {search_party} region')
    # print(details.Party)
    # print(details.Candidate)
    # if index == search_region and details.Party == search_party:
    #     print('yes')
    #     print(f'{details.Candidate} had {details.Votes} in {search_region} region')

# if search_party:
#     print(dictt[search_party])
#     print(dictt['Candidate'][1])
# if search_party in all_party:
#     heading.color('black')
#     heading.goto(-115, 459)
#     heading.write(f"Regional Details")
#
#     result_data = data[data.Party == search_party]
#     print(result_data)
#     # result_data1 = data[data.Region == search_region]
#     result.color("red")
#     result.goto(int(result_data.x), int(result_data.y))
#     result.write(f"{result_data.Candidate.item()} \n  {result_data.Party.item()} \n {result_data.Votes.item()}", font=("Courier", 16, "bold"))
#
#     a = 0
#     for detail in details:
#         all_result.color('green')
#         all_result.goto(detail)
#         all_result.write(f"{all_candidate[a]} \n {all_votes[a]}")
#         a += 1
#
#


screen.exitonclick()

