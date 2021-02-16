import os
import json


# Configuration file
settings_path = "/home/anton/Desktop/screenshot/many-screenshots/settings.json"

settings = 0

# Reading configuration file
with open(settings_path) as f:
    settings = json.load(f)

source_path = settings["source_path"] + settings["source_naming_pattern"] + "." + settings["extension"]
destination_path = settings["destination_path"] + settings["destination_naming_pattern"] + "." + settings["extension"]
if source_path:
    # Moving file as per configuration file settings
    os.rename(source_path, destination_path)

# Step3 - learn how to import the py file contents


# HERE COME MY PLANS AND IDEAS

# Future steps - I need to compare captions with file names