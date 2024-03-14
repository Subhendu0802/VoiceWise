from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
#from webdriver_manager.chrome import ChromeDriverManager
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--use-fake-ui-for-media-stream')
chrome_options.add_argument('--headless=new')
#chrome_options.headless=True
driver=webdriver.Chrome(options=chrome_options)
website=r"F:\assistant\VoiceWise\data\voice.html"

driver.get(website)

def Listen():
    print("Listening...")
    #driver.get(website)
    driver.find_element(by=By.ID,value='start').click()
    while 1:
        text=driver.find_element(by=By.ID,value='output').text
        if text !="":
            print("you said: "+text)
            driver.find_element(by=By.ID,value='end').click()
            return text
if __name__=="main":        
    while 1:
        Listen()


