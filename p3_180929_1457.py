#!/usr/bin/env python3
#p3_180929_1457.py
# Overloading add function

class objectA:
    def __init__(self, value):
        self.value = value
    def __add__(self, objectB):
        self.value += objectB
        return self.value
    def getValue(self):
        print(self.value)

def main():
    a = objectA(194)
    a = objectA(a + 81)
    a.getValue()

if __name__ == '__main__':
    main()
