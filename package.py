import json
executeconfig = ""

try:
    f = open('package.json', 'r')
    buildconfig = json.load(f)
    f.close()
except:
    print("Error reading 'Package.json' file.")

if buildconfig['removepreviousbuilts'] == True:
    executeconfig = "@echo off\ndel Build\nmkdir Build"

for files in buildconfig["filesandfolders"]:
    print(buildconfig["filesandfolders"][files])
    executeconfig = executeconfig + "\ncopy " + buildconfig["filesandfolders"][files] + " Build"


if buildconfig['usePyinstaller'] == True :
    executeconfig = executeconfig + "\ncd Build\nmkdir out\nECHO Building exe...\npyinstaller.exe --onefile " + buildconfig["Pyinstallerfile"]

executeconfig = executeconfig + "\nECHO Build compleated.\ndel builder.bat\ncd .."

builder = open('builder.bat','w')
builder.write(executeconfig)
builder.close