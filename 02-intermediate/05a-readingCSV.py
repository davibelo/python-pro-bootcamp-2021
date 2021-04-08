import pandas as pd
# https://pandas.pydata.org/

import csv

# with csv
with open("02-intermediate/05b-weather_data.csv") as data_file:
    data0 = csv.reader(data_file)
    temperatures = []
    for row in data0:
        if row[1] != "temp":
            temperatures.append(int(row[1]))

print("a)", temperatures)

# with pandas
data = pd.read_csv("02-intermediate/05b-weather_data.csv")
print("b)", data)
print("c)", type(data))
print("d)", data["temp"])

data_dict = data["temp"].to_dict()
print("e)", data_dict)

temp_list = data["temp"].to_list()
print("f)", temp_list)

average = sum(temp_list) / len(temp_list)
print("g)", average)

# with panda mean method
print("h)", type(data["temp"]))
avg = data["temp"].mean()
print("i)", avg)
