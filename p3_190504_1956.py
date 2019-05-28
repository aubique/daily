#!/usr/bin/env python3
#p3_190504_1956.py
# Draft for console jw_quiz_bot game
# OOP implementation

import sqlite3
import shelve
from random import sample, randint

SHELVE_FILE = 'files/p3_190504_1956_shelve'
HISTORY = 'hist'
CORRECT = 'corr'

class Ticket:
    """
    Class represents a dictionary of jw-quiz format
    Which practically is: question, correct answer, list of other answers
    _self.ca is a correct answer
    {'Q': _question, 'CA': _correct_answer, 'A': [*_other_answers]}
    """

    def __init__(self, *args):
        """Initialize a ticket if there any argumets given"""
        if args:
            self.set_ticket_from_args(*args)

    def show_ticket(self):
        """Show this ticket"""
        print(self.get_ticket_as_dict())

    def get_ticket_as_mixed_tuple(self):
        """Return a list of question and mixed answers"""
        answers = (self.ca, *self.oa)
        return (self.q, *sample(answers, len(answers)))

    def get_ticket_as_dict(self):
        """Return a dictionary from this ticket"""
        return self.args_to_dict(self.q, self.ca, *self.oa)

    def args_to_dict(self, question, correct, *answers):
        """Convert parameters to the dictionary and return it"""
        return {'Q': question, 'CA': correct, 'OA': answers}

    def set_ticket_from_varargs(self, varargs):
        """Not in use"""
        self.q, self.ca, *self.oa = varargs

    def set_ticket_from_args(self, question, correct, *answers):
        """
        Save parameters to this ticket
        Final method to write down the new question
        """
        self.q = question
        self.ca = correct
        self.oa = answers

    def set_ticket_from_dict(self, d):
        """
        Save the given dictionary to this ticket
        Extract dictionary and pass to the function of writing down new data
        :param d: (dict) Dictionary of jw-quiz format
        """
        self.set_ticket_from_args(d['Q'], d['CA'], *d['OA'])

class Core:
    def __init__(self, uid=0):
        self.db = DB()
        self.uid = str(uid)
        self.quiz_len = self.db.count_rows()
    def open_shelve_as(self, callback_func, *callback_args):
        self.storage: shelve.DbfilenameShelf
        with shelve.open(SHELVE_FILE) as self.storage:
            return callback_func(*callback_args)
    def get_question(self):
        if self.question_index is None:
            #TODO: send END message
            return None
        qt: tuple = self.db.get_ticket_by_id(self.question_index)
        # Unpack a tuple without ID primary key
        # Ticket(question, correct, *answers)
        self.ticket = Ticket(*qt[1:])
        self.set_user_game()
        self.ticket.show_ticket()
        return self.ticket.get_ticket_as_mixed_tuple()
    def set_question_index_as_random(self):
        try:
            history = self.storage[self.uid+HISTORY]
            history_len = len(history)
        except KeyError:
            print('\n\t// KEY ERROR //\n\tget_question_index()\n')
            history = []
            history_len = 0
        questions_left = self.quiz_len - history_len
        print('QUESTION LEFT:\t\t({}q)'.format(questions_left))
        if questions_left:
            while True:
                num = randint(0, self.quiz_len-1)
                if not str(num) in history:
                    print('get_question_randnum():\t#{}'.format(num))
                    self.question_index = num
                    return num
        else:
            self.question_index = None
    def get_answer(self):
        return self.get_correct_from_shelve()
    def get_correct_from_shelve(self):
        try:
            return self.storage[self.uid+CORRECT]
        except KeyError:
            return None
    def update_history(self):
        pass
    def set_user_game(self):
        self.storage[self.uid+CORRECT] = [self.question_index, self.ticket.ca]
        print('Game Mode: Enabled')
    def finish_user_game(self):
        del self.storage[self.uid+CORRECT]
        print('Game Mode: Disabled')

def main():
    show_question()
    check_answer()

def show_question():
    game = Core()
    game.open_shelve_as(game.set_question_index_as_random)
    question, *answers = game.open_shelve_as(game.get_question)
    print(question)
    print(answers)

def check_answer():
    game = Core()
    question_index, correct = game.open_shelve_as(game.get_answer)
    if correct:
        if correct == input():
            print('Right')
            game.open_shelve_as(game.update_history)
        else:
            print('Wrong')

def input_question():
    a = list()
    print('Type question:')
    #q = input()
    q = 'field_question'
    for i in range(4):
        print('Type answer #{}:'.format(i))
        #a.append(input())
        a.append('field_answer'+str(i))
    return (q, *a)

def input_question_tuple(self, ticket):
    (ticket.q, ticket.ca, ticket.a1, ticket.a2, ticket.a3) = self.input_question()
    return ticket

class DB:
    def __init__(self):
        self.conn = sqlite3.connect('files/p3_190504_1956.db')
        self.c = self.conn.cursor()
        self.new_table()
    def new_table(self):
        with self.conn:
            self.c.execute("""
                           CREATE TABLE IF NOT EXISTS quiz (
                           id integer primary key,
                           question text,
                           correct text,
                           answer1 text,
                           answer2 text,
                           answer3 text)
                           """)
    def insert_ticket(self, ticket):
        with self.conn:
            self.c.execute(
                """INSERT INTO quiz(question, correct, answer1, answer2, answer3)
                VALUES (:question, :correct, :answer1, :answer2, :answer3)""",
                {'question': ticket.q,
                 'correct': ticket.ca,
                 'answer1': ticket.a1,
                 'answer2': ticket.a2,
                 'answer3': ticket.a3},
            )
    def get_ticket_by_question(self, question):
        with self.conn:
            self.c.execute('SELECT * FROM quiz WHERE question=?', (question,))
                           #{'q': question})
            return self.c.fetchall()
    def get_ticket_by_id(self, qid):
        with self.conn:
            # second argument of execute is a tuple
            self.c.execute('SELECT * FROM quiz WHERE ID=?', (qid,))
            return self.c.fetchone()
    def remove_ticket_by_question(self, question):
        with self.conn:
            self.c.execute('DELETE from quiz WHERE quiz = :?', (question))
                           #{'q': question})
    def select_all_rows(self):
        """Select all rows from _quiz table"""
        with self.conn:
            tmp = self.c.execute('SELECT * FROM quiz').fetchall()
            #TODO: Clean it up
            #print(tmp)
            return tmp
    def count_rows(self):
        """Return a number of rows in _quiz table"""
        with self.conn:
            return len(self.select_all_rows())

if __name__ == '__main__':
    main()
