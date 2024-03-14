import requests
from bs4 import BeautifulSoup

classes=["zCubwf","hgKElc","LTKOO sY7ric","Z0LcW","gsrt vk_bk FzvWSb YwPhnf","pclqee","tw-Data-text tw-text-small tw-ta",
    "IZ6rdc","O5uR6d LTKOO","vlzY6d","webanswers-webanswers_table__webanswers-table",
    "dDoNo ikb4Bb gsrt","sXLaOe","LWkfKe","VQF4g","qv3Wpe","kno-rdesc"]
useragent='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36'

def Online_Scrapper(query,PRINT=True):
    query=query.replace(" + "," plus ")
    query=query.replace(" - "," minus ")
    URL = "https://www.google.com/search?q=" + query
    headers={'User_Agent': useragent}
    page =requests.get(URL,headers=headers)
    soup=BeautifulSoup(page.content,'html.parser')
    for i in classes:
        try:
            result=soup.find(class_=i).get_text()
            if PRINT:
                print("by class",i)
            return result
        except Exception:
            pass
    return "No idea about that"
print(Online_Scrapper("weather",True))