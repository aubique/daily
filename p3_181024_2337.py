#!/usr/bin/env python3
#p3_181024_2337.py
# Using OOP-paradighm
# Lesson: 1.What is TKinter

from tkinter import *

class Block:
    def __init__(self, master):
        self.e = Entry(master, width=20)
        self.b = Button(master, text="Преобразовать")
        self.l = Label(master, bg='black', fg='white', width=20)
        self.e.pack()
        self.b.pack()
        self.l.pack()
    def setFunc(self, func):
        self.b['command'] = eval('self.' + func)
    def strToSortList(self):
        s = self.e.get()
        s = s.split()
        s.sort()
        self.l['text'] = ' '.join(s)
    def strReverse(self):
        s = self.e.get()
        s = s.split()
        s.reverse()
        self.l['text'] = ' '.join(s)

def main():
    root = Tk()

    first_block = Block(root)
    first_block.setFunc('strToSortList')

    second_block = Block(root)
    second_block.setFunc('strReverse')

    root.mainloop()

if __name__ == '__main__':
    main()
