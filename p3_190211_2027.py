#!/usr/bin/env python3
#p3_190211_2027.py
# Simple Telegram bot, version #1
#https://api.telegram.org/bot690888180:AAEWVPgNKXnUEVyOG77F9xDAf7JdaQ-29eg/getupdates
#chatid: 680120849

import requests
import json

TOKEN = '690888180:AAEWVPgNKXnUEVyOG77F9xDAf7JdaQ-29eg'
URL = 'https://api.telegram.org/bot' + TOKEN + '/'

def get_updates():
    url = URL + 'getupdates'
    response = requests.get(url)
    return response.json()

def get_message():
    data = get_updates()
    chat_id = data['result'][-1]['message']['chat']['id']
    message_text =  data['result'][-1]['message']['text']

def main():
    get_message()
    with open('p3json_190211_2027.json', 'w') as file:
        json.dump(get_updates(), file, indent=2, ensure_ascii=False)

if __name__ == '__main__':
    main()
