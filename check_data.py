import pandas as pd

menu_hrs_df = pd.read_csv("./data/menu_hours.csv")
store_status_df = pd.read_csv("./data/store_status.csv")
timezones_df = pd.read_csv("./data/timezones.csv")

print(timezones_df.isna().sum())