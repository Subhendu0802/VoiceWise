import pyttsx3
from threading import Thread
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('rate',175)
engine.setProperty('voice',voices[0].id)

def Speak(*args,**kwargs):
    audio=""
    for i in args:
        audio+=str(i)
    print(audio)
    engine.say(audio)
    engine.runAndWait()
    
