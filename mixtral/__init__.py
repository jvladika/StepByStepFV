import random

from hugchat import hugchat
from hugchat.login import Login
from dotenv import load_dotenv
import time
import os

import os
from together import Together

load_dotenv()


def login(hugging_face_email, cookie_path_dir="./cookies_snapshot"):
    sign = Login(hugging_face_email, None)
    cookies = sign.loadCookiesFromDir(cookie_path_dir)

    return hugchat.ChatBot(cookies=cookies.get_dict())


def prompt(chatbot, message, web=False):

    client = Together(api_key=os.environ.get("TOGETHER_API_KEY"))

    formated_message =  [
                {
                    "role": "user",
                    "content": message
                }
            ]

    response = client.chat.completions.create(
        #model="meta-llama/Meta-Llama-3.1-70B-Instruct-Turbo",
        model="mistralai/Mixtral-8x7B-Instruct-v0.1",
        temperature=0.05,
        max_tokens = 256,
        top_p = 1.0,
        frequency_penalty=0.0,
        presence_penalty=0.0,
        messages=formated_message
    )
    resp = response.choices[0].message.content
    resp = resp.replace("\n", " ")
    
    return resp

"""
def prompt(chatbot, message, web=True):
    if not web:
        time.sleep(8)
        big_sleep = random.uniform(0, 1)
        if big_sleep > 0.9:
            print("big sleep")
            time.sleep(random.randint(30, 60))

    response = chatbot.chat(message, web_search=web, _stream_yield_all=True)

    print(response.wait_until_done())

    if web:
        return response

    return response.text
"""