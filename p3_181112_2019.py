#!/usr/bin/env python3
#p3_181112_2019.py
# Tkinter. Lesson 8
# Events

import tkinter as tk

class FocusedWindow:
    def __init__(self, master):
        self.master = master
        self.create_interface()
        self.pack_interface()
    def create_interface(self):
        self.e1 = tk.Entry(self.master)
        self.e2 = tk.Entry(self.master)
        self.b = tk.Button(self.master, text='Change')
        self.l = tk.Label(self.master, text='Text here')
    def pack_interface(self):
        self.e1.pack()
        self.e2.pack()
        self.b.pack()
        self.l.pack()
        self.b.bind('<Button-1>', self.change_label_size)
        self.b.bind('<Return>', self.change_label_size)
        self.b.bind('<FocusIn>', lambda event, focus=1: self.focus_handler(event, focus))
        self.b.bind('<FocusOut>', lambda event, focus=0: self.focus_handler(event, focus))
    def change_label_size(self, event):
        new_width = self.e1.get()
        new_height = self.e2.get()
        self.l.config(width=self.e2.get(), height=self.e2.get())
    def focus_handler(self, event, focus):
        if focus:
            self.l.config(bg='white')
        else:
            self.l.config(bg='lightgrey')

def main():
    root = tk.Tk()
    win1 = FocusedWindow(root)
    root.mainloop()

if __name__ == '__main__':
    main()
