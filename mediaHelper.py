# module to work with folders
import os
from pathlib import Path

SSD_PATH = "/Volumes/Extreme SSD"

if not os.path.exists(SSD_PATH):
    print(f"SSD {SSD_PATH} is not plugged in ")
    exit()

print(SSD_PATH)

destinationFolder = input('Enter the name of the new foflder: ')
newFolderPath = os.path.join(SSD_PATH, destinationFolder)

print(f'Destination path is {newFolderPath}')

# mkdirs creates all the intermediate directories if they do not exist
# the exist_ok=True parameter prevents an error if the directory already exists
os.makedirs(newFolderPath, exist_ok=True)

subfolders = ["pics", "videos", "projectFiles"]

for subfolder in subfolders:
  os.makedirs(os.path.join(newFolderPath, subfolder), exist_ok=True)

print("✅ All folders created successfully!")