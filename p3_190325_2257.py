#!/usr/bin/env python3
#p3_190325_2257.py
# WWTBAM game
# CLI-based model

import json
import re
from random import sample

PATTERN = r'^\d'
VALID = 'correct'
NOT_VALID = 'wrong'

class WWTBAM:
    def __init__(self):
        self.jsondata = self.load_questions()
    def load_questions(self):
        # Load tickets in JSON format from the file
        with open('files/WWTBAM1.json', 'r') as f:
            #print(f.closed)
            jsondata = json.load(f)
            return jsondata
    def get_ticket(self, num):
        # Get a ticket consisting 1 question and 4 answers
        return self.jsondata[num]
    def mix_answers(self, old_ticket):
        # Mix up the answers in the ticket
        correct_answer = old_ticket['A'][0]
        new_ticket = old_ticket
        new_answers = sample(old_ticket['A'], len(old_ticket['A']))
        new_ticket['A'] = new_answers
        return new_ticket, correct_answer
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
            self.print_result(VALID, answer_index_output)
        else:
            self.print_result(NOT_VALID, answer_index_output)
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
    t = cli_app.get_ticket(0)
    t, a = cli_app.mix_answers(t)
    cli_app.show_ticket(t)
    cli_app.verify_answer(t, a)

if __name__ == '__main__':
    main()
