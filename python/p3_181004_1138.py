#!/usr/bin/env python3
#p3_181004_1138.py
# Calculate amount of snow by using operator-overloading
# https://younglinux.info/oopython/operators.php

import sys

class Snow:
    def __init__(self, amount):
        self.amount = amount
    def __add__(self, n):
        self.amount += n
    def __sub__(self, n):
        self.amount -= n
    def __mul__(self, n):
        self.amount *= n
    def __truediv__(self, n):
        self.amount /= n
    def getAmount(self):
        print(self.amount)
    def makeSnow(self, col):
        rows = int(self.amount / col)
        lastLine = self.amount % col
        for i in range(rows):
            for j in range(col):
                sys.stdout.write('*')
            sys.stdout.write('\n')
        for i in range(lastLine):
            sys.stdout.write('*')
        sys.stdout.write('\n')

def main():
    s1 = Snow(15)
    s1 + 4
    s1.getAmount()
    s1.makeSnow(4)

if __name__ == '__main__':
    main()
