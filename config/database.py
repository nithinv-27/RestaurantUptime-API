from pymongo.mongo_client import MongoClient
import urllib 
import os
from dotenv import load_dotenv
import pandas as pd

# menu_hrs_df = pd.read_csv("./data/menu_hours.csv")
# store_status_df = pd.read_csv("./data/store_status.csv")
# timezones_df = pd.read_csv("./data/timezones.csv")

load_dotenv("keys.env")

username = os.getenv("USER_NAME")
password = os.getenv("PASSWORD")

# Encode the username and password for safe URL usage
username = urllib.parse.quote_plus(f"{username}")  # Add your MongoDB username
password = urllib.parse.quote_plus(f"{password}")  # Add your MongoDB password

# MongoDB connection URI (Replace Cluster0 with your actual MongoDB cluster/app name)
uri = "mongodb+srv://{}:{}@Cluster0.scone.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0".format(username, password)

# # Create a new MongoDB client and establish a connection to the server
# client = MongoClient(uri)

# # Specify the database to use
# mydb = client["restaurants_database"]

# # Menu Hours CSV
# menu_hrs_collection = mydb["menu_hours"]

# menu_hrs_collection.insert_many(menu_hrs_df.to_dict(orient="records"))

# # Store Status CSV
# store_status_collection = mydb["store_status"]

# store_status_collection.insert_many(store_status_df.to_dict(orient="records"))

# # Timezones CSV
# timezones_collection = mydb["timezones"]

# timezones_collection.insert_many(timezones_df.to_dict(orient="records"))