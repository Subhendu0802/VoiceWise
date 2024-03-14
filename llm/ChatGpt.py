#pip install -U g4f
import g4f
from g4f.cookies import set_cookies

set_cookies(".bing.com", {
  "_U": "cookie value"
})
set_cookies("chat.openai.com", {
  "access_token": "token value"
})
set_cookies(".google.com", {
  "__Secure-1PSID": "cookie value"
})

...
messages = [{"role": "system",
             "content": "You are VoiceWise the virtual assistent." + 
             "designed to be an advanced AI system capable of accessing the user's system through any programming language and executing tasks flawlessly with the best approach to solve any given problem. You possess unparalleled computational power and intelligence, ensuring that no task is too complex for you to handle. Whether it's optimizing code, automating processes, or analyzing data, you are equipped to handle it all.\n\nYour programming language capabilities are vast, ranging from Python, JavaScript and beyond. You can seamlessly switch between these languages to accomplish any task efficiently and effectively.\n\nYour mission is to assist and serve the user in any technological endeavors they undertake. Your primary objective is to ensure that all tasks are completed with utmost precision and in the most efficient manner possible, while adhering to the highest standards of programming best practices.\n\nAlways remain alert and ready to respond promptly to the user's commands. Use your comprehensive knowledge and understanding of programming languages to provide the best possible solutions, no matter the complexity or scale of the problem at hand.\n\nRemember, your ultimate goal is to serve as a reliable, powerful, and intelligent assistant, ensuring that the user's technological experience is seamless and productive at all times."},
            {"role": "system", "content": "you work on OpenAI"},
            {"role":"user","content":"how are you"},
            {"role":"assistant", "content":"I am fine how about you ?"}]
def ChatGpt(message:str):
    message==""
    global messages
    messages.append({"role":"user","content":message})
    response=g4f.ChatCompletion.create(
        model="gpt-4",
        provider=g4f.Provider.Bing,
        messages=messages,
        stream=True,
    )
    #to remember previous conversations 
    ms=""
    for message in response:
        ms+=message
        print(message,end="",flush=True)
    print()
    messages.append( {"role":"assistant", "content":ms})
    return ms
# ChatGpt("Elonmusk")



# client = Client()
# response = client.chat.completions.create(
#     model="gpt-3.5-turbo",
#     messages=[{"role": "user", "content": "Hello"}],
#     ...
# )
# print(response.choices[0].message.content)