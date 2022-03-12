import base64
print("----------------------------------------CHN Whiteboard----------------------------------------")
print("Image to URL converter for CHN Whiteboard\nhttps://chnsoftwaredevelopers.com/")
print("----------------------------------------CHN Whiteboard----------------------------------------\n")
while True:
    file = input("Enter the filename of the image you want to convert to a data URL (Type 'H' for help.) : ")
    if file.strip().lower() == "h":
        print("Image to URL converter for CHN Whiteboard - Help :\n")
        print("You can enter the file name of the image with the file path as follows, \n\n")
        print("    Eg : C:\\Users\\user1\\Pictures\\myimg.png")
        print("\nThe data URL will be saved as a text file in the same directory where the image exists.\n\n")
        print("    Eg : C:\\Users\\user1\\Pictures\\myimg.png.txt")
    else:
        try:
            dataURL = base64.b64encode(open(file, "rb").read())
            dataURL = dataURL.decode('utf-8')
            dataURL = "data:image/png;base64," + dataURL
            print("-------------------------------------------Data URL-------------------------------------------")
            print(dataURL)
            print("-------------------------------------------Data URL-------------------------------------------")
            outputFile = file + ".txt"
            f = open(outputFile, "w")
            f.write(str(dataURL))
            f.close()
        except Exception as e:
            print(e)
