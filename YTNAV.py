                                                                
import speech_recognition as sr  
import keyboard                                                                    
def record():
    r = sr.Recognizer()
    f = sr.Recognizer()
    with sr.Microphone() as source:
        print("Speak:")                                                                                   
        audio = r.record(source, duration = 2.5)   
    try:
        print("You said " + r.recognize_google(audio))
    except sr.UnknownValueError:
        print("Could not understand audio")
        record()        
    if r.recognize_google(audio)=="play" or r.recognize_google(audio)=="stop":
        keyboard.press_and_release("k")
    if r.recognize_google(audio)=="forward":
        keyboard.press_and_release("right arrow") 
    if r.recognize_google(audio)=="rewind":
        keyboard.press_and_release("left arrow")
    if r.recognize_google(audio)=="next":
        keyboard.press_and_release("shift + n")
    if r.recognize_google(audio)=="sound":
        keyboard.press_and_release("m")
    if r.recognize_google(audio)=="find":
        keyboard.press_and_release("ctrl + k")
        with sr.Microphone() as source:
            print("Search:")                                                                                   
            s=f.record(source, duration = 3)
            search = f.recognize_google(s)
        try:
            print("You said " + search)
            keyboard.write(search,delay=0.1)
            keyboard.press_and_release("enter")
        except sr.UnknownValueError:
            print("Could not understand audio")
        record()    
    if r.recognize_google(audio)=="captions":
        keyboard.press_and_release("c")
    if r.recognize_google(audio)=="full screen":
        keyboard.press_and_release("f")
    if r.recognize_google(audio)=="Mini":
        keyboard.press_and_release("i")
    if r.recognize_google(audio)=="theatre":
        keyboard.press_and_release("t")    
def do():
    while window:
        record()
from tkinter import *
window = Tk()
window.title("YTNAV")
window.geometry("400x300")
button_frame = Frame(window, width = 250, height = 50)
button_frame.pack(padx = 10, pady = 10)
Listen_button = Button(button_frame, text = "Listen", width = 35,
font = ('arial',10,'bold'), fg = "red" ,command = do)
Listen_button.grid(row = 4, column = 0, padx = 2, pady = 2)
window.mainloop()