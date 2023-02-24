# get points by list for faster searching
import pandas as pd

first_names = ["Matthew", "Ben"]
last_names = ["Smallhouse", "Charleston"]

points_list = pd.read_csv("FIS-points-list-AL-2023-363.csv")
info = points_list[["Lastname", "Firstname", "SLpoints", "GSpoints"]]

people = pd.DataFrame()
for first, last in zip(first_names, last_names):
    new_info = info[(info["Lastname"].str.lower() == last.lower()) & (info["Firstname"].str.lower() == first.lower())]
    people = pd.concat([people, new_info])

print(people)