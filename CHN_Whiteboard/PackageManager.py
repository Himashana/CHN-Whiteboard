from tqdm import tqdm
import requests

chunk_size = 1024

canvas_setup = "https://chnsoftwaredevelopers.com/CHN-Classroom/Whiteboard/v1.2.0/CHN_Whiteboard/canvas_setup.js"

print("CHN Whiteboard Package manager")
print("______________________________________________________________________")
print("")
package = input("Package : ")
x = package
r = requests.get(canvas_setup, stream = True)
if x == "canvas_setup --install" :
        print("canvas_setup.js : Installing...")       
        total = int(r.headers['content-length'])

        with open("canvas_setup.js", 'wb') as f:
                for data in tqdm(iterable = r.iter_content(chunk_size = chunk_size), total = total/chunk_size, unit='KB'):
                        f.write(data)

        print("canvas_setup.js : Installed successfully!")
        print("______________________________________________________________________")

else:
        print("______________________________________________________________________")  

exit_program = input("Exit -> Enter")
