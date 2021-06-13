import webbrowser
from tkinter import*

f = open("service.js", "a")
i = open("info.txt", "a")
x = 0
y = 0
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



def Update():
    Window1.destroy()
    #---------------------------Window 2-------------------------
    Window2 = Tk()
    Window2.title("CHN Whiteboard Update assistant")

    windowWidth = Window2.winfo_reqwidth()
    windowHeight = Window2.winfo_reqheight()
    #Window1.geometry("600x400")
    Window2.eval('tk::PlaceWindow . center')
    positionRight = int(Window2.winfo_screenwidth()/2 - windowWidth/2)
    positionDown = int(Window2.winfo_screenheight()/2 - windowHeight/2)

    Window2.geometry("+{}+{}".format(positionRight, positionDown))

    Label1 = Label(Window2, text="CHN Whiteboard Update assistant")
    Label2 = Label(Window2, text="                                                   ")
    Label3 = Label(Window2, text="       ")
    Label4 = Label(Window2, text="  ")
    Label5 = Label(Window2, text="This setup will guid you to install the latest")
    Label6 = Label(Window2, text="version of CHN Whiteboard.")
    Button1 = Button(Window2, text="Install", command = Update)

    Label1.grid(row = 0, column = 0, sticky = W, pady = 2)
    Label2.grid(row = 1, column = 0, sticky = W, pady = 2)
    Label3.grid(row = 1, column = 1, sticky = W, pady = 2)
    Label4.grid(row = 1, column = 2, sticky = W, pady = 2)
    Label5.grid(row = 2, column = 0, sticky = W, pady = 2)
    Label6.grid(row = 3, column = 0, sticky = W, pady = 2)
    Button1.grid(row = 4, column = 1, sticky = W, pady = 2)


#---------------------------Window 1-------------------------
Window1 = Tk()
Window1.title("CHN Whiteboard Update assistant")

windowWidth = Window1.winfo_reqwidth()
windowHeight = Window1.winfo_reqheight()
#Window1.geometry("600x400")
Window1.eval('tk::PlaceWindow . center')
positionRight = int(Window1.winfo_screenwidth()/2 - windowWidth/2)
positionDown = int(Window1.winfo_screenheight()/2 - windowHeight/2)

Window1.geometry("+{}+{}".format(positionRight, positionDown))

Label1 = Label(Window1, text="CHN Whiteboard Update assistant")
Label2 = Label(Window1, text="                                                   ")
Label3 = Label(Window1, text="       ")
Label4 = Label(Window1, text="  ")
Label5 = Label(Window1, text="This setup will guid you to install the latest")
Label6 = Label(Window1, text="version of CHN Whiteboard.")
Button1 = Button(Window1, text="Next>", command = Update)

Label1.grid(row = 0, column = 0, sticky = W, pady = 2)
Label2.grid(row = 1, column = 0, sticky = W, pady = 2)
Label3.grid(row = 1, column = 1, sticky = W, pady = 2)
Label4.grid(row = 1, column = 2, sticky = W, pady = 2)
Label5.grid(row = 2, column = 0, sticky = W, pady = 2)
Label6.grid(row = 3, column = 0, sticky = W, pady = 2)
Button1.grid(row = 4, column = 1, sticky = W, pady = 2)



break_line = input("")

mainloop()