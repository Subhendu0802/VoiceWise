from func.Chat import Chat
from func.SpeakOnline import Speak
#from func.SpeakOffline import Speak
from func.ListenJs import Listen
from func.DataOnline2 import Online_Scraper
from llm.ChatGpt import ChatGpt
from mtranslate import translate
from colorama import Fore, Back, Style
if  __name__ == '__main__':
    while 1:
        Q=Listen()
        Q=translate(Q)
        #print(f"{Fore.LIGHTRED_EX} {Q}")
        QL=Q.lower()
        # GetChat=Chat(QL)
        # GetData=Online_Scraper(Q)
        # if GetData != None:
        #     Speak(GetData)
        # else:
        #     Speak(GetChat[0])
        reply=ChatGpt(Q)
        Speak(reply)
