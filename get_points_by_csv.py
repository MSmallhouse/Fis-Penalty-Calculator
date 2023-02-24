# get points by list for faster searching
import pandas as pd

EVENT = "SL"
CSV = "FIS-points-list-AL-2023-363.csv"

first_names = ["Matthew", "Ben"]
last_names = ["Smallhouse", "Charleston"]

points_list = pd.read_csv(CSV)
info = points_list[["Lastname", "Firstname", EVENT+"points"]]

relevant_points = pd.DataFrame()
for first, last in zip(first_names, last_names):
    #new_info = info[(info["Lastname"].str.lower() == last.lower()) & (info["Firstname"].str.lower() == first.lower())]
    new_info = info[(info["Lastname"].str.lower() == last.lower()) & (info["Firstname"].str.lower() == first.lower())]
    new_info = info.loc[(info["Lastname"].str.lower() == last.lower()) & (info["Firstname"].str.lower() == first.lower()), EVENT+"points"]
    relevant_points = pd.concat([relevant_points, new_info])

print(relevant_points)