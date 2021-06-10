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
			desc="Initializing...",
			ascii=False, ncols=75):
	time.sleep(0.01)

print("CHN Account - Login")
print("_______________________________________________________________")
print("")
User = input("Username : ")
Pass = input("Password : ")

final_url = "https://chnsoftwaredevelopers.com/Software_Web_Pages/Whiteboard.php?user=" + User + "&pass=" + Pass
r = requests.get(final_url)
print(r.text)
#webbrowser.open(final_url)
s = input("")
