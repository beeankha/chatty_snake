from voice_control import voice_to_text
import webbrowser


while True:
    print("Python is listening...")
    inp = voice_to_text()

    print(f"You just said {inp}.")
    
    if inp == "stop listening":
        print("Goodbye!")
        break

    elif "Google search" in inp:
        inp = inp.replace("Google search ","")
        webbrowser.open("http://google.com/search?q="+inp)
        continue
