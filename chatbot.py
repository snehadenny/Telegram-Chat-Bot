import requests
import time
from aiengine import *
bot_token=""

sneha=SNEHA()
def get_data(offset):
    recieve_url=f"https://api.telegram.org/bot{bot_token}/getUpdates?offset={offset}"
    response=requests.get(recieve_url)
    data=response.json()

    return {"chat_id":data["result"][-1]["message"]["from"]["id"],
        "text":data["result"][-1]["message"]["text"]}

def get_latest_offset():
    recieve_url=f"https://api.telegram.org/bot{bot_token}/getUpdates"
    response=requests.get(recieve_url)
    return response.json()["result"]#[-1]["update_id"]

def send_message(chat_id,text):
    send_url=f"https://api.telegram.org/bot{bot_token}/sendMessage?chat_id={chat_id}&text={text}"
    response=requests.get(send_url)
    return response.json()

offset=get_latest_offset()
print(offset)
while True:
    latest_offset=get_latest_offset()
    if latest_offset!=offset:
        result=get_data(latest_offset)
        #print("From:",result["chat_id"],"text:",result["text"])
        msg=result["text"]
        chat_id=result["chat_id"]
        reply=sneha.chat(msg)

        send_message(chat_id,reply)
        offset=latest_offset
    time.sleep(0.5)



   
