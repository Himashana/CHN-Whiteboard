import webbrowser
f = open("service.js", "a")
i = open("info.txt", "a")
x = 0
y = 0
print("    |||||||||  |||      |||")
print("   |||||||     |||      |||")
print("  ||||||       |||      |||")
print(" ||            ||||||||||||")
print("||             ||||||||||||")
print(" ||            ||||||||||||")
print("  ||||||       |||      |||")
print("   |||||||     |||      |||")
print("    |||||||||  |||      |||")
while x == 0 :
    open = input("Do you want to start 'service.js' javascript(y/n)? ")
    if open == "y" or open == "Y" :
    
        f.truncate(0)
        f.write('')
        

        webbrowser.open("https://chnsoftwaredevelopers.com/")
        webbrowser.open("Whiteboard.html")
        
        print("Started succesfully")
        print("Updates - 0%")
        print("Application is running in your browser")
        
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
            print("Setup successfully")
            setup_compleate = input("")
        else:
            f.truncate(0)
            f.write('location.replace("stoped.html");')
            f.close()
            break;
    else :
        print("Error occured : Undefined")
