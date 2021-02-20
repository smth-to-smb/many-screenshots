import os
import config

settings = config.settings()

source_path = settings["source_path"] + settings["source_naming_pattern"] + "." + settings["extension"]
destination_path = settings["destination_path"] + settings["destination_naming_pattern"] + "." + settings["extension"]
if source_path:
    # Moving file as per configuration file settings
    os.rename(source_path, destination_path)

# Next step - solve the numeration issue



# HERE COME MY PLANS AND IDEAS

# Future steps - I need to compare captions with file names