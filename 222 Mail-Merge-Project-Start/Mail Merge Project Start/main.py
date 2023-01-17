import csv
with open("../226 weather-data.csv") as weather_data:
    data = csv.reader(weather_data)
    tem = []
    for row in data:
        if row[1] != "temp":
            tem.append(int(row[1]))

print(tem["temp"])