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

def createDestinationFolderName():
  name = input("Enter the name of the main folder: ".strip())
  add_date = input("Would you like to add todays date at the beginning of the folder name? (y/n): ").strip().lower() in ('y')
  if add_date:
    name = f"{datetime.today().strftime('%Y-%m-%d')}_{name}"
  print("Main folder name is ", name)
  return name

def chooseDevice(devices)->Path:
  #iterates over all the folders that are within the volumes path
  # skipping other files
  if not devices:
      print('No deviсes were found')
      exit()
  for i, device in enumerate(devices, start=1):
      print(f"{i}. {device.name}")
  while True:
      try:
          choice = int(input("Enter the number of the device you want to choose: ").strip())
          if 1 <= choice <= len(devices):
            return devices[choice - 1]
      except ValueError:
          print('Something went wrong with your input. Please try again.')

def createSubfoders(create, DEFAULT_SUBFOLDERS):
  subfolders = []
  if create == 'y':
    subfolders = DEFAULT_SUBFOLDERS
  else:
     exit()
  print("We have some suggested subfolders, those are:")
  printSubfolders(subfolders)
  inputSubfolders = input("Type 'y' to use the suggested ones, or 'n' to create your own: ").lower()
  if(inputSubfolders == 'n'):
    subfolders  = getSubfolders()
  print("The following subfolders will be created:")
  printSubfolders(subfolders)
  for sub in subfolders:
    (newFolderPath / sub).mkdir(exist_ok=True)
  print("✅ All destination folders were created successfully!")

def copySonyPictures(origin: Path, destination: Path):
   print( f"Copying Sony pictures from {origin} to {destination}... (not implemented)")
   print("Pictures at the sony camera are")
   all_pictures = [p for p in origin.glob("*.ARW") if not p.name.startswith("._")]
   for pic in all_pictures:
       print(pic.name)
   
def copySonyVideos(origin: Path, destination: Path):
    print(f"Copying Sony videos from {origin} to {destination}... (not implemented)")


def copyFiles(origin: Path, destination: Path):
    # This function would contain logic to copy files from origin to destination
    print(f"Copying files from {origin} to {destination}... (not implemented)")
    if not origin.exists():
        print(f"Origin path {origin} does not exist.")
        return
    if origin.stem == 'Sony':
       copySonyPictures(origin / "DCIM" / "100MSDCF", destination)
      #  copySonyVideos()
   
devices = [v for v in VOLUMES_PATH.iterdir() if v.is_dir()]

destination_device = chooseDevice(devices)
print(f"Selected device is {destination_device}")

# 3️⃣ Ask for the new folder name
folderName = createDestinationFolderName()

# 4️⃣ Build the full path
newFolderPath = VOLUMES_PATH /destination_device / folderName


# 5️⃣ Create main folder (exist_ok=True avoids errors if it already exists)
# parents=True creates the filders in the middle if they did not exist
newFolderPath.mkdir(parents=True, exist_ok=True)

if input("Would you like to create some subfolders at the new folder? (y)").lower() == 'y':
    createSubfoders('y', DEFAULT_SUBFOLDERS)

print("Now we are going to select the latest footage you have on your device/s")

origin_device = chooseDevice(devices)
print(f"Selected device where your footage is stored: {origin_device}")
print("We will proceed to copy files from the origin device to the new folder.")
copyFiles(origin_device, newFolderPath/DEFAULT_SUBFOLDERS[0])  # Assuming we copy to the first subfolder 'pics'
