import os
import json


# Configuration file
settings_path = "/home/anton/Desktop/screenshots/settings.json"

settings = 0

# Reading configuration file
with open(settings_path) as f:
    settings = json.load(f)

# Moving file as per configuration file settings
os.rename(settings["source_path"], settings["destination_path"])

# Step2 - learn how to import the py file contents
