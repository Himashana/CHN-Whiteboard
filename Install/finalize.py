import webbrowser
from tqdm import tqdm
import requests
import webbrowser
import time
import requests



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


for i in tqdm (range (100),
			desc="Preparing files...",
			ascii=False, ncols=75):
	time.sleep(0.01)

for i in tqdm (range (13),
			desc="Verifying files...",
			ascii=False, ncols=75):
	time.sleep(0.01)
for i in tqdm (range (100),
			desc="Downloading updates...",
			ascii=False, ncols=75):
	time.sleep(0.01)
for i in tqdm (range (100),
			desc="Cleaning up...",
			ascii=False, ncols=75):
	time.sleep(0.10)	
for i in tqdm (range (100),
			desc="Initializing...",
			ascii=False, ncols=75):
	time.sleep(0.01)
print("_______________________________________________________________")
xxx = input("Please make sure you have an active internet connection to verify your account. click enter to continue...")
print("_______________________________________________________________")
print("")
print("CHN Account - Login")

User = input("Username : ")
Pass = input("Password : ")
print("_______________________________________________________________")
print("Verifying your account...")

final_url = "https://chnsoftwaredevelopers.com/Software_Web_Pages/Whiteboard.php?user=" + User + "&pass=" + Pass
r = requests.get(final_url)
data = r.text

print("_______________________________________________________________")
print(r.text)
if data == "CHN Whiteboard Activated" :
        print("_______________________________________________________________")
        print("congratulation! CHN Whiteboard ready to use. See CHN Whiteboard installation guid [https://chnsoftwaredevelopers.com/CHN-Classroom/Whiteboard/CHN-Whiteboard-install-assistant/] to launch CHN Whiteboard.")
        print("_______________________________________________________________")
elif data == "CHN Whiteboard activating..." :
        print("_______________________________________________________________")
        print("congratulation! CHN Whiteboard ready to use. See CHN Whiteboard installation guid [https://chnsoftwaredevelopers.com/CHN-Classroom/Whiteboard/CHN-Whiteboard-install-assistant/] to launch CHN Whiteboard.")
        print("_______________________________________________________________")
else:
        print("_______________________________________________________________")
        print("If you don't have a CHN Account go to https://chnsoftwaredevelopers.com/Register/Register.html to create your CHN account. Then restart CHN Whiteboard setup to login again!")
        print("_______________________________________________________________")
#webbrowser.open(final_url)
s = input("")

