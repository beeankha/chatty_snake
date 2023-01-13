import speech_recognition as sr
import webbrowser


speech = sr.Recognizer()

def voice_to_text():
    voice_input = ""

    with sr.Microphone() as source:
        speech.adjust_for_ambient_noise(source)
        try:
            audio = speech.listen(source)
            voice_input = speech.recognize_google(audio)
        except sr.UnknownValueError:
            pass
        except sr.RequestError:
            pass
        except sr.WaitTimeoutError:
            pass

    return voice_input

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
