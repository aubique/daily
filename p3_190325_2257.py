#!/usr/bin/env python3
#p3_190325_2257.py
# WWTBAM game
# CLI app model

import json
import re
from random import sample, randint

JSON_IDS = { "512": [0], "513": [0] }
PATTERN = r'^\d'
VALID = 'correct'
NOT_VALID = 'wrong'
UID = 512

class WWTBAM:
    def __init__(self):
        self.jsondata = self.load_json('quiz')
    def load_json(self, func):
        # Load JSON data from file
        with open('files/p3_190325_2257_{}.json'.format(func), 'r') as f:
            #print(f.closed)
            return json.load(f)
    def save_json(self, func, data):
        # Save JSON data to the file
        with open('files/p3_190325_2257_{}.json'.format(func), 'w') as f:
            json.dump(data, f, ensure_ascii=False, indent=4)
    def start_game_loop(self):
        # Game ends by the last question
        quiz = self.mixup(self.jsondata)
        for ticket in quiz:
            a = self.get_correct_answer(ticket)
            t = self.mix_answers(ticket)
            self.show_ticket(t)
            self.verify_answer(t, a)
    def get_quiz_lindex(self, quiz):
        # Get an index of the last question loaded in json-format
        return self.index_dec(len(quiz))
    def start_game_for_loop(self):
        # Randomly chosen question
        quiz = self.jsondata
        user_id = str(512)
        msg_history = json.loads(json.dumps(JSON_IDS))
        #print(type(msg_history))
        if user_id in msg_history:
            for i in range(len(quiz)):
                if not i in msg_history[user_id]:
                    #print(i)
                    t = self.get_ticket(i)
                    a = self.get_correct_answer(t)
                    t = self.mix_answers(t)
                    self.show_ticket(t)
                    self.verify_answer(t, a)
    def start_game_while_loop(self):
        quiz = self.jsondata
        quiz_len = len(quiz)
        user_id = str(512)
        msg_history = json.loads(json.dumps(JSON_IDS))
        # If user_id exists in dictionary of player-id's
        if user_id in msg_history:
            # Number of game loops
            iter_num = quiz_len - len(msg_history[user_id])
            for i in range(iter_num):
                while True:
                    random_num = randint(0, self.index_dec(len(quiz)))
                    print(random_num)
                    if not random_num in msg_history[user_id]:
                        msg_history[user_id].append(random_num)
                        #self.save_json('msg', msg_history)
                        break
        #while(True):
        #    print(randint(0, len(quiz)))
        #t = self.get_ticket(randint(0, last))
    def start_game_one_pass(self):
        # Game does only one pass asking one question
        msg_history = self.load_json('msg')
        quiz = self.load_json('quiz')
        quiz_len = len(quiz)
        user_id = str(UID)
        # If there are any questions which aren't asked yet
        tickets_left = quiz_len - len(msg_history[user_id])
        if (user_id in msg_history) and tickets_left:
            while True:
                random_num = randint(0, self.index_dec(len(quiz)))
                print(str(random_num)+'\t\t randint(0, len(quiz))')
                # In order to avoid repeating the same question
                # Check if _random_num is already listed in message history
                # In case it is not listed launch question add _random_num to the history
                if not random_num in msg_history[user_id]:
                    self.launch_ticket(quiz, random_num)
                    msg_history[user_id].append(random_num)
                    self.save_json('msg', msg_history)
                    break
    def launch_ticket(self, quiz, num):
        ticket = quiz[num]
        a = self.get_correct_answer(ticket)
        t = self.mix_answers(ticket)
        self.show_ticket(t)
        result, guess = self.verify_answer(t, a)
        self.print_result(result, guess)
    def get_ticket(self, quiz, num):
        # Get a ticket consisting 1 question and 4 answers
        return quiz[num]
        #return self.jsondata[num]
    def mix_quiz(self, quiz):
        # Mixing the question sequence in the game
        return self.mixup(quiz)
    def mix_answers(self, ticket):
        # Mix up the answers in the ticket
        ticket['A'] = self.mixup(ticket['A'])
        return ticket
    def mixup(self, list_of_items):
        # Mix up the items in the given array
        return sample(list_of_items, len(list_of_items))
    def get_correct_answer(self, ticket):
        return ticket['A'][0]
    def get_question(self, ticket):
        # Extract a question from the given ticket
        return ticket['Q']
    def get_answers(self, ticket):
        # Get all the questions listed in the ticket
        return ticket['A']
    def get_answer_n(self, ticket, num):
        # Get a certain answer by its number
        return ticket['A'][num]
    def show_ticket(self, ticket):
        # Display inward data of the given ticket
        question = self.get_question(ticket)
        answers = self.get_answers(ticket)
        text_lines = 'Question:\t\t' + question
        for i in range(4):
            text_lines += '\nAnswer #{}:\t\t{}'.format(self.index_inc(i), answers[i])
        print(text_lines)
    def verify_answer(self, ticket, answer_correct):
        # Validation check of the player's answer
        print('Enter the correct answer:')
        answer_index_output = self.check_input(input())
        answer_index = self.index_dec(answer_index_output)
        answer = self.get_answer_n(ticket, answer_index)
        #print('answer_index_output={}; answer={}; answer_correct={}'.format(
        #    answer_index_output, answer, answer_correct))
        if answer in answer_correct:
            return VALID, answer_index_output
        else:
            return NOT_VALID, answer_index_output
    def check_input(self, data):
        # Regexp integrity check of the input data
        crypto = re.search(PATTERN, data)
        if crypto:
            return int(crypto.group())
        return None
    def print_result(self, result_msg, num):
        print('You have chosen the answer #{}. Your answer is {}!'.
              format(num, result_msg))
    def index_inc(self, i):
        # Increasing for readable output
        # [1-4] slices instead of [0-3] indeces
        return i + 1
    def index_dec(self, i):
        # Decreasing for readable output
        return i - 1

def main():
    cli_app = WWTBAM()
    cli_app.start_game_one_pass()

if __name__ == '__main__':
    main()
