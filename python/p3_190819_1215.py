#!/usr/bin/env python3
# p3_190819_1215.py
# CodeWars: Persistent Bugger
# Details: Write a function, persistence, that takes in a positive
# parameter num and returns its multiplicative persistence, which is the
# number of times you must multiply the digits in num until you reach a
# single digit.

def convert_to_int_list(number: int):
    # Split number into a list of integers
    return [int(nlist) for nlist in str(number)]

def persistence(n: int):
    steps = 0
    while not len(str(n)) < 2:
        j = 1
        # Mulitply every digit in number
        for i in convert_to_int_list(n):
            j = j * i
        # Check if it's one-digit-number
        steps += 1
        # Set a new var for list
        n = j
    return steps

if __name__ == '__main__':
    print(persistence(999))
