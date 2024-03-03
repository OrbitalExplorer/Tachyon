from modlistCreation import modlistCreation
from prepareExport import prepareExport
import os

modrinthCofigPath = modlistCreation().split(os.path.sep)[:-1] # Get profile.json path and remove profile.json and turn el in list
prepareExport(modrinthCofigPath)

profileName = modrinthCofigPath[-1]
print(f'\n\n{profileName.capitalize()} is ready to export!')
input('')