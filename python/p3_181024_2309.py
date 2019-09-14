#!/usr/bin/env python3
#p3_181024_2309.py
# Introdution to TKinter

from tkinter import *

root = Tk()
e = Entry(root, width=20)
b = Button(root, text="Преобразовать")
l = Label(root, bg='black', fg='white', width=20)

def strToSortList(event):
    s = e.get()
    s = s.split()
    s.sort()
    l['text'] = ' '.join(s)

b.bind('<Button-1>', strToSortList)
e.pack()
b.pack()
l.pack()
root.mainloop()
