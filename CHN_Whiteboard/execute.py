#Supported Whiteboard version : v1.3.0
from tqdm import tqdm
import requests
import webbrowser
import time


f = open("service.js", "a")
i = open("info.txt", "a")
x = 0
y = 0

chunk_size = 1

url = "https://chnsoftwaredevelopers.com/CHN-Classroom/Whiteboard/CHN-Whiteboard-install-assistant/Update.py"

r = requests.get(url, stream = True)


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
update = input("Required to download 'update.py' updates(recommended). If you continue, this will automatically download updates(Make sure you have an active internet connection). ")
print("_______________________________________________________________")
for i in tqdm (range (241),
			desc="Preparing files...",
			ascii=False, ncols=75):
	time.sleep(0.01)
	
print("Ready to download updates.")
print("_______________________________________________________________")

total = int(r.headers['content-length'])
with open("Update.py", 'wb') as d:
    for data in tqdm(iterable = r.iter_content(chunk_size = chunk_size), total = total/chunk_size, unit='KB'):
        d.write(data)
print("Updated successfully!")
print("_______________________________________________________________")

c_f_url = "https://chnsoftwaredevelopers.com/CHN-Classroom/Whiteboard/CHN-Whiteboard-install-assistant/Update.php?v=1.2.0"
r = requests.get(c_f_url)
data = r.text
print("")
print(r.text)
print("")

if(r.text == "You are up to date!"):
    x = 0
else:
    x = 1
    execute_update = input("")

while x == 0 :
    open = input("Do you want to start 'service.js' javascript(y/n)? ")
    if open == "y" or open == "Y" :
    
        f.truncate(0)
        f.write('')
        
        #webbrowser.open("https://chnsoftwaredevelopers.com/")
        webbrowser.open("Whiteboard.html")
        
        print("Started succesfully")
        print("Application is running in your browser")

        print("_______________________________________________________________")
        print("Enter 'stop()' to stop 'service.js' javascript")
        print("_______________________________________________________________")
        
        while y == 0 :
            stop = input("")
            if stop == "stop()" :
              stop_confirm = input("Click enter to stop 'sevice.js' javascript")  
              f.truncate(0)
              f.write('location.replace("stoped.html");')
              f.close()
              x = 1
              y = 1
              break;
            else :
                print("Error occured : Undefined")
    elif open == "n" or open == "N":
        print("Exit()")
        exit = input("")
        if exit == "setup.start --whiteboard" :
            f.truncate(0)
            f.write('location.replace("stoped.html");')
            f.close()
            print("service.js - Overwrite")
            i.truncate(0)
            i.write('CHN_Whiteboard - v1.2.0')
            i.close()       
            print("Created info.txt")
            print("_______________________________________________________________")
            print("Setup successfully")
            setup_compleate = input("")
            break;
        else:
            f.truncate(0)
            f.write('location.replace("stoped.html");')
            f.close()
            break;
    else :
        print("Error occured : Undefined")
