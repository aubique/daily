#!/usr/bin/env python3
#p3_190212_2243.py
# Telegram bot calculator
# Bot model without webhooks

import requests
import re
REGEXP = '\d+\s*[\+\-\*\/]{1}\s*\d+'

class Calculator:
    def __init__(self):
        token = '690888180:AAEWVPgNKXnUEVyOG77F9xDAf7JdaQ-29eg'
        self.url_bot = 'https://api.telegram.org/bot' + token + '/'
        self.regex = re.compile(REGEXP)
    def get_updates(self):
        url = self.get_url('getUpdates', None)
        resp = requests.get(url)
        return resp.json()
    def get_message(self):
        data = self.get_updates()
        last_message = data['result'][-1]
        chat_id = last_message['message']['from']['id']
        message_text = last_message['message']['text']
        message_info = {'room_id': chat_id, 'msg_text': message_text}
        return message_info
    def send_message(self, cid, text):
        message_args = {'room_id': cid, 'msg_text': text}
        url = self.get_url('sendMessage', message_args)
        check_code = requests.get(url)
    def get_url(self, request, params):
        url = self.url_bot + request
        if params:
            cid = params['room_id']
            text = params['text']
            url += '?chat_id={}&text={}'.format(cid, text)
        return url
    def calculate(self, message):
        exp1 = list()
        exp1 = re.findall(self.regex, message)
        if exp1:
            print(eval(exp1[0]))

def main():
    win1 = Calculator()
    print(win1.get_message())

if __name__ == '__main__':
    main()
