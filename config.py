import os
import json


def settings():

    # Configuration file
    settings_path = "/home/anton/Desktop/screenshot/many-screenshots/settings.json"

    settings = 0

    # Reading configuration file
    with open(settings_path) as f:
        settings = json.load(f)

    return settings

