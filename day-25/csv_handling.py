#with open("weather_data.csv") as weather_data:
#    data = weather_data.readlines()
#    print(data)
#comment out is ctrl + k + c
import csv
# # with open("weather_data.csv") as weather_data:
# #     data = csv.reader(weather_data)
# #     tempratures = []
# # #     for row in data:
# #         if row[1] != "temp":
# #             tempratures.append(int(row[1]))
# #     print(tempratures)

import pandas


data = pandas.read_csv("weather_data.csv")
# temp_list = data["temp"].to_list()
maximum_temp = data["temp"].max()
print(maximum_temp)
print(data.temp == data.temp.max)
sum = 0
monday = data[data.day == "Monday"]
print(monday.condition)
# for i in temp_list:
#     sum += i
# avg_temp = sum/len(temp_list)
# print(avg_temp)
# print(type(data))
# data_dict = data.to_dict()
# print(data_dict)
# print(data.condition)
# print(data.temp)
# print(data.day)

## create a data frame from scratch
data_dict = {
    "students": ["Amy", "James", "Angela"],
    "scores": [75, 82, 43]
}
data_from_scratch = pandas.DataFrame(data_dict)
data_from_scratch.to_csv("new_data_csv")



