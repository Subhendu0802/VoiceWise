import pyttsx3
from ListenJs import Listen
from threading import Thread
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('rate',175)
engine.setProperty('voice',voices[0].id)

IS_HOT_WORD=False
HOT_WORD_Detect_IS_ON=True

def HOT_WORD_Detect():
    global IS_HOT_WORD, HOT_WORD_Detect_IS_ON
    while True:
        if  HOT_WORD_Detect_IS_ON:
            user_input=Listen().lower()

            if "Hey" in user_input:
                IS_HOT_WORD=True
                #HOT_WORD_Detect_IS_ON=False
                return
        else:
            return

def Speak(*args,**kwargs):
    audio=""
    for i in args:
        audio+=str(i)
    print(audio)
    engine.say(audio)
    engine.runAndWait()

HOT_WORD_Detect_IS_ON=True
HOT_WORD_Detect()
    
