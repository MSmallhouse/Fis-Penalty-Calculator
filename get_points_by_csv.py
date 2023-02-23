# get points by list for faster searching
import pandas as pd

first_names = ["Matthew", "Ben"]
last_names = ["Smallhouse", "Charleston"]

points_list = pd.read_csv("FIS-points-list-AL-2023-363.csv")
info = points_list[["Lastname", "Firstname", "SLpoints", "GSpoints"]]


for first, last in zip(first_names, last_names):
    my_info = info[(info["Lastname"].str.lower() == last.lower()) & (info["Firstname"].str.lower() == first.lower())]

    print(my_info)