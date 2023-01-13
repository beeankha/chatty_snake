import os
import pathlib
import platform

from voice_control import voice_to_text

directory = pathlib.Path.cwd()

def open_file(filename):
    if platform.system() == "Windows":
        os.system(f"explorer {directory}\\files\\{filename}")
    elif platform.system() == "Darwin":
        os.system(f"open {directory}/files/{filename}")
    else:
        os.system(f"xdg-open {directory}/files/{filename}")

while True:
    print("Python is listening...")
    inp = voice_to_text().lower()

    print(f"You just said {inp}.")
    
    if inp == "stop listening":
        print("Goodbye!")
        break

    elif "open pdf" in inp:
        inp = inp.replace("open pdf ","")
        myfile = f'{inp}.pdf'
        open_file(myfile)
        continue

    elif "open text file" in inp:
        inp = inp.replace("open text file ","")
        myfile = f'{inp}.txt'
        open_file(myfile)
        continue
