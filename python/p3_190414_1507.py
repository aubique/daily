#!/usr/bin/env python3
#p3_190414_1507.py
# Shelve data excercise №1
# Workaround with KeyError exception and callback

import shelve
SHELVE_FILE = 'files/p3_190414_1507'

def static_update_shelve(number, data):
    """
    Update an existing shelve or create a new one
    :param number: Index of item for Shelve DB
    :param data: The data information to put into the Shelve DB
    :return: (list) Return an arroy of the Shelve DB
    """
    with shelve.open(SHELVE_FILE) as storage:
        try:
            history = storage[number]
            history.append(data)
            storage[number] = history
        except KeyError:
            print('\n\nKEY ERROR\n\n')
            storage[number] = list(data)
        finally:
            print(storage[number])
            return storage

def dynamic_update_shelve(number, callback, *cb_args):
    with shelve.open(SHELVE_FILE) as storage:
        history = storage[number]
        #print(*cb_args)
        callback(history, *cb_args)

def check_quiz(history, cid):
    if not str(cid) in history:
        print('{} is not listed in the shelve'.format(cid))
        return history
    else:
        print('It is listed')
        return None

def main():
    cid = '680120848'
    data = str(1)
    static_update_shelve(cid, data)
    dynamic_update_shelve(cid, check_quiz, 1)

if __name__ == '__main__':
    main()
