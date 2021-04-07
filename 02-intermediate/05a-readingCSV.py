import pandas as pd
# https://pandas.pydata.org/

import csv

with open("02-intermediate/05b-weather_data.csv") as data_file:
    data = csv.reader(data_file)
    temperatures = []
    for row in data:
        if row[1] != "temp":
            temperatures.append(int(row[1]))

print(temperatures)


data2 = pd.read_csv("02-intermediate/05b-weather_data.csv")
print(data2)
print(type(data2))
print(data2["temp"])