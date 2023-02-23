# get points by list for faster searching
import pandas as pd
# MS FILTER FIRST AND LAST NAMES TO GET RID OF CAPITALS
first = "Matthew"
last = "smallhouse"

first = first.lower()
last = last.lower()

points_list = pd.read_csv("FIS-points-list-AL-2023-363.csv")
info = points_list[["Lastname", "Firstname", "SLpoints", "GSpoints"]]
info["Lastname"] = info["Lastname"].apply(str.lower)
info["Firstname"] = info["Firstname"].apply(str.lower)

my_info = info[(info["Lastname"] == last) & (info["Firstname"] == first)]

print(my_info)