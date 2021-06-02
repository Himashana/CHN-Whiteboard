import webbrowser
f = open("service.js", "a")
x = 0
y = 0
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
        open = input("")
        f.truncate(0)
        f.write('location.replace("stoped.html");')
        f.close()
        break;
    else :
        print("Error occured : Undefined")
