#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#p3_190405_2159.py
# Work out with ReplyKeyboard buttons of pyTelegramBotApi

import telebot
from telebot.types import Message, ReplyKeyboardMarkup, ReplyKeyboardRemove, Update
import requests
from flask import Flask, request
from flask_sslify import SSLify

#https://api.telegram.org/bot892470673:AAH9nJrcqo5dzx8mA_Zthap7Pi-n7G7jlf8/setWebhook?url=
TOKEN = '892470673:AAH9nJrcqo5dzx8mA_Zthap7Pi-n7G7jlf8'
QUESTION = 'Type number three:'
CORRECT = '3'
ANSWERS = ['124', '3', '1488', '4012837']
bot = telebot.TeleBot(TOKEN)
app = Flask(__name__)
sslify = SSLify(app)

def generate_markup(message:Message, q:str, la:list):
    markup = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    markup.add(*la)
    #[markup.add(i) for i in a]
    bot.send_message(message.chat.id, q, reply_markup=markup)

@app.route('/', methods=['POST', 'GET'])
def webhook():
    if request.headers.get('content-type') == 'application/json':
        json_string = request.get_data().decode('utf-8')
        update = Update.de_json(json_string)
        bot.process_new_updates([update])
        return ''
    else:
        flask.abort(403)

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message:Message):
    message.text: str
    bot.send_message(message.chat.id, 'Game is started')
    generate_markup(message, QUESTION, ANSWERS)

@bot.message_handler(func=lambda message: True, content_types=['text'])
def check_answer(message:Message):
    ca : str = CORRECT
    la : list = ANSWERS
    keyboard_hidden = ReplyKeyboardRemove()
    if message.text == ca:
        #bot.send_message(message.chat.id, 'Right!', reply_markup=keyboard_hidden)
        bot.reply_to(message, 'Right!', reply_markup=keyboard_hidden)
    else:
        #bot.send_message(message.chat.id, 'Wrong!', reply_markup=keyboard_hidden)
        bot.reply_to(message, 'Wrong', reply_markup=keyboard_hidden)

def main():
    pass

if __name__ == '__main__':
    app.run()
