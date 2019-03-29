#!/usr/bin/env python3
#p3_190211_2027.py
# Telegram bot showing the exchange rate of BTC
#https://api.telegram.org/bot690888180:AAEWVPgNKXnUEVyOG77F9xDAf7JdaQ-29eg/getupdates
#chatid: 680120849

import requests
import json
from time import sleep

TOKEN = '690888180:AAEWVPgNKXnUEVyOG77F9xDAf7JdaQ-29eg'
URL = 'https://api.telegram.org/bot' + TOKEN + '/'

# Keep ID of latest message to discover new messages
global last_update_id
last_update_id = 0

def get_updates():
    url = URL + 'getupdates'
    response = requests.get(url)
    return response.json()

def get_message():
    global last_update_id
    data = get_updates()
    # JSON: result(list)->lastitem->message(dict)->chat(dict)->id(int)/text(str)
    last_message = data['result'][-1]
    msg_id = last_message['update_id']

    if last_update_id != msg_id:
        last_update_id = msg_id
        chat_id = last_message['message']['chat']['id']
        msg_text = last_message['message']['text']
        message_info = {'room_id': chat_id, 'message_text': msg_text,
                        'message_id': msg_id}
        return message_info
    return None

def send_message(room_id, message_text='Loading...'):
    url = URL + 'sendmessage?chat_id={}&text={}'.format(room_id, message_text)
    check_code = requests.get(url)
    # In case request isn't sent (code!=200)
    if 200 != check_code.status_code:
        print(check_code)

def decode_to_json(data=get_updates(), filename='files/p3json_190211_2027.json'):
    with open(filename, 'w') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

def send_thesame_message():
    chat = get_message()
    print('LAST MESSAGE = ', chat)
    answer = 'Bot says: ' + chat['message_text']
    send_message(chat['room_id'], answer)

def handler_module_btc():
    while True:
        message = get_message()
        if message:
            text = message['message_text']
            chat_id = message['room_id']
            if text == '/btc':
                send_message(chat_id, get_btc())
        sleep(5)

def get_btc():
    url = 'https://yobit.net/api/2/btc_usd/ticker'
    resp = requests.get(url).json()
    price = resp['ticker']['last']
    return str(price) + ' usd'

def main():
    handler_module_btc()

if __name__ == '__main__':
    main()
