#!/usr/bin/env python3
#p3_181025_1216.py
# Calculator
# Lesson: 1. What's the TKinter?

from tkinter import *

class Window:
    def __init__(self, master):
        self.e1 = Entry(master, width=5)
        self.e2 = Entry(master, width=5)
        self.b1 = Button(master, text="+", command=self.buttonAddition)
        self.b2 = Button(master, text="-", command=self.buttonSubtraction)
        self.b3 = Button(master, text="*", command=self.buttonMultiplication)
        self.b4 = Button(master, text="/", command=self.buttonDivision)
        self.l = Label(master, bg='black', fg='white', width=20)
        self.createInterface()
    def createInterface(self):
        self.e1.grid(row=1, column=1, rowspan=2)
        self.e2.grid(row=1, column=4, rowspan=2)
        self.b1.grid(row=1, column=2)
        self.b2.grid(row=2, column=2)
        self.b3.grid(row=1, column=3)
        self.b4.grid(row=2, column=3)
        self.l.grid(row=3, column=1, columnspan=4)
    def calculate(self, operation):
        x, y = self.getValues()
        msgError = None

        if operation == '+':
            result = x + y
        elif operation == '-':
            result = x - y
        elif operation == '*':
            result = x * y
        elif operation == '/':
            if y == 0:
                msgError = "Division by zero"
            else:
                result = x / y
        else:
            msgError = "Not valid operator"
        if msgError:
            self.l["text"] = msgError
            result = None
        else:
            strResult = "{} {} {} = {}".format(x, operation, y, result)
            self.l["text"] = strResult

        return result
    def getValues(self):
        x = int(self.e1.get())
        y = int(self.e2.get())
        return x, y
    def buttonAddition(self):
        self.calculate('+')
    def buttonSubtraction(self):
        self.calculate('-')
    def buttonMultiplication(self):
        self.calculate('*')
    def buttonDivision(self):
        self.calculate('/')

def main():
    root = Tk()
    win1 = Window(root)
    root.mainloop()

if __name__ == '__main__':
    main()
