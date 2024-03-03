import pandas
import csv
squirrel_data_main_csv = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

squirrel_count = open("squireel_count.csv", "a", newline="")
output = csv.writer(squirrel_count)


