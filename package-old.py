import json

def writeData(data):
    f = open('package.json', 'w')
    json.dump(data, f, indent=4)
    f.close()

dataDict = {}
appName = input('App name : ')
dataDict['app-Name'] = appName

version = input('Version : ')
dataDict['version'] = version

Description = input('Description : ')
dataDict['description'] = Description

homepage = input('Home page : ')
dataDict['homepage'] = homepage

author = input('Author : ')
dataDict['author'] = author

programmingLanguage = input('Programming Language : ')
dataDict['programmingLanguage'] = programmingLanguage


write = input('Are you sure you want to make package.json(Y/N): ').strip().lower()

if write == 'y':
    writeData(dataDict)
    print(dataDict)

input('Click enter to exit.')