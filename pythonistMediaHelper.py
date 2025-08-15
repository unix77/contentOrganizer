from pathlib import Path
from datetime import datetime
import platform

VOLUMES_PATH = Path("/Volumes")
DEFAULT_SUBFOLDERS = ["pics", "videos", "projectFiles"]

def printSubfolders(subfolders):
   for sub in subfolders:
      print(sub)

def getSubfolders():
  subfolders = []
  while True:
      subfolderName = input("Type a subfolder name, press enter when finished. ").strip()
      print(f"Entered subfolder name is {subfolderName}")
      if subfolderName == '':
        return subfolders
      else:
         subfolders.append(subfolderName)

def createMainFolderName():
  name = input("Enter the name of the main folder: ".strip())
  add_date = input("Would you like to add todays date at the beginning of the folder name? (y/n): ").strip().lower() in ('y')
  if add_date:
    name = f"{datetime.today().strftime('%Y-%m-%d')}_{name}"
  print("Main folder name is ", name)
  return name

def chooseDevice(devices):
  #iterates over all the folders that are within the volumes path
  # skipping other files
  if not devices:
      print('No devides were found')
      exit()
  for i, device in enumerate(devices, start=1):
      print(f"{i}. {device.name}")
  while True:
      try:
          choice = int(input("Enter the number of the device where you want to copy your footage"))
          if 1 <= choice <= len(devices):
            return devices[choice - 1]
      except ValueError:
          print('Something went wrong with your input. Please try again.')

def createSubfoders(create, DEFAULT_SUBFOLDERS):
  subfolders = []
  if create == 'y':
    subfolders = DEFAULT_SUBFOLDERS
  print("We have some suggested subfolders, those are:")
  printSubfolders(subfolders)
  inputSubfolders = input("Type 'y' to use the suggested ones, or 'n' to create your own: ").lower()
  if(inputSubfolders == 'n'):
  subfolders  = getSubfolders()
  print("The following subfolders will be created:")
  printSubfolders(subfolders)
  for sub in subfolders:
  (newFolderPath / sub).mkdir(exist_ok=True)
  print("✅ All folders created successfully!")
   


devices = [v for v in VOLUMES_PATH.iterdir() if v.is_dir()]

destination_device = chooseDevice(devices)
print(f"Selected device is {destination_device}")

# 3️⃣ Ask for the new folder name
folderName = createMainFolderName()

# 4️⃣ Build the full path
newFolderPath = VOLUMES_PATH / folderName

# 5️⃣ Create main folder (exist_ok=True avoids errors if it exists)
# parents=True creates the filders in the middle if they did not exist
newFolderPath.mkdir(parents=True, exist_ok=True)

createSubfoders = input("Would you like to create some subfolders at the new folder? (y)").lower()
