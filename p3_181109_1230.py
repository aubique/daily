#!/usr/bin/env python3
#p3_181109_1230.py
# Tkinter. Lesson 5
# Radiobutton, Checkbutton, variables

import tkinter as tk
ADDRESS_BOOK = [
    ("Dmitry", "+74985300196"),
    ("Thomas", "+33708744015"),
    ("Vlad", "+79167042238")
]

class AddressBook:
    def __init__(self, master):
        self.f_left = tk.Frame(master)
        self.f_right = tk.Frame(master)
        self.createInterface()
        self.packInterface()
    def createInterface(self):
        self.varPhone = tk.StringVar()
        self.varPhone.set(None)
        for tmpText, tmpPhone in ADDRESS_BOOK:
            self.b = tk.Radiobutton(self.f_left, text=tmpText, variable=self.varPhone,
                    value=tmpPhone, indicatoron=0, command=self.setText, width=20, height=3)
            self.b.pack(side=tk.TOP)
        self.l = tk.Label(self.f_right, text="Phone number", width=30, height=10)
        self.f_left.pack(side=tk.LEFT)
        self.f_right.pack(side=tk.LEFT)
        self.l.pack(side=tk.TOP)
    def packInterface(self):
        pass
    def setText(self):
        self.l.config(text=self.varPhone.get())

def main():
    root = tk.Tk()
    win1 = AddressBook(root)
    root.mainloop()

if __name__ == '__main__':
    main()
