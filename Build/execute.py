#Supported Whiteboard version : v1.3.0

print("Loading application...", end="\r")
try:
    from PyQt5.QtCore import QUrl
    from tqdm import tqdm
    import requests
    import webbrowser
    import time
    import sys
    from PyQt5.QtCore import *
    from PyQt5. QtWidgets import *
    from PyQt5.QtWebEngineWidgets import *
    import pathlib
except Exception as e:
    print(e)

class mainApplication(QMainWindow):
    def __init__(self):
        super(mainApplication, self).__init__()
        self.version = "1.3.1"
        self.WhitOpenFilePath = None

    def downloadUpdater(self):
        chunk_size = 1
        url = "https://chnsoftwaredevelopers.com/CHN-Classroom/Whiteboard/CHN-Whiteboard-install-assistant/Update.py"
        r = requests.get(url, stream = True)

        for i in tqdm (range (11), desc="Preparing files...", ascii=False, ncols=75):
	        time.sleep(0.01)
   
        total = int(r.headers['content-length'])
            
        with open("Update.py", 'wb') as d:
            for data in tqdm(iterable = r.iter_content(chunk_size = chunk_size), total = total/chunk_size, unit='KB'):
                d.write(data)

    def checkForUpdates(self):
        checkForUpdatesURL = "https://chnsoftwaredevelopers.com/CHN-Classroom/Whiteboard/CHN-Whiteboard-install-assistant/Update.php?v=" + self.version
        r = requests.get(checkForUpdatesURL)
        updateStatus = r.text
        return updateStatus        

    def getFilePath(self):
        #Return file path as a URL
        self.WhitOpenFilePath = pathlib.Path().resolve()
        self.WhitOpenFilePath = str(self.WhitOpenFilePath) + '/index.html'
        self.WhitOpenFilePath = self.WhitOpenFilePath.replace('\\', '/')
        self.WhitOpenFilePath = "file:///" + self.WhitOpenFilePath
        return self.WhitOpenFilePath

    def displayWhiteboard(self):
        self.browser = QWebEngineView()
        self.browser.setUrl(QUrl(self.WhitOpenFilePath))
        self.setCentralWidget(self.browser)
        self.showMaximized()

print("_______________________________________________________________")
print("")
print("        _______      _        _       _       _")
print("       / /____/     / /_____ / /     /  \    / /")
print("      / /          /  _____   /     / /\ \  / /")
print("     / /_____     / /      / /     / /  \ \/ /")
print("    /_______/    /_/      /_/     /_/    \ _/")
print("             CHN Software Developers")
print("_______________________________________________________________")
print("")
update = input("Required to download 'update.py' self updater(recommended). If you continue, this will automatically download updates(Make sure you have an active internet connection). ")
print("_______________________________________________________________")

Whiteboard = QApplication(sys.argv)
QApplication.setApplicationName('CHN Whiteboard v1.3.1')
app = mainApplication()

updateAvailable = False

try:
    print("Ready to download updates.")
    print("_______________________________________________________________")
    app.downloadUpdater()
    print("Self updater downloaded successfully!")
    print("_______________________________________________________________")
except:
    print("Download error[Self updater] : Error")
    print("_______________________________________________________________")
    input()
    quit()

try:
    updateStatus = app.checkForUpdates()
    print("\n" + updateStatus + "\n")
    if(updateStatus == "You are up to date!"):
        updateAvailable = False
    else:
        updateAvailable = True
        input()
        exec(open("Update.py").read())
except:
    print("Error check for updates[Self updater] : Error")
    print("_______________________________________________________________")
    input()
    quit()

#Open service.js file
f = open('service.js', 'w')

if updateAvailable == False:
    while True:
        open = input("Do you want to start CHN Whiteboard [this will overwrite 'service.js' javascript(y/n)]? ").strip().lower()
        if open == "y":
            try:
                f.write("")
                print("Starting...", end="\r")
                filePath = app.getFilePath()
                app.displayWhiteboard()
                print("Started succesfully")
                print("Application is running[" + filePath + "]...")
            except Exception as startError:
                print('Error [ ' + str(startError) + ' ] : unable to start the application.')
                input()

            print("_______________________________________________________________")
            print("Enter 'stop()' to stop CHN Whiteboard.")
            print("_______________________________________________________________")
            while True:
                stop = input("> ").strip().lower()
                if stop == "stop()":
                    input("Click enter to stop the application.")
                    f.write('location.replace("stoped.html");')
                    quit()
                else :
                    print("Error occured : Undefined")
            
        elif open == "n":
                input("Click enter to exit.")  
                break;
        else:
            print("Error occured : Undefined")
#Close service.js file.
f.close()