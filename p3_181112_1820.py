#!/usr/bin/env python3
#p3_181112_1820.py
# Tkinter. Lesson 7
# Method bind()

import tkinter as tk

class windowTextList:
    def __init__(self, master):
        self.createInterface(master)
        self.packInterface()
    def createInterface(self, master):
        self.e = tk.Entry(master)
        self.lb = tk.Listbox(master)
    def packInterface(self):
        self.e.pack(side=tk.TOP)
        self.lb.pack(side=tk.TOP)
        self.e.bind('<Return>', self.copyToList)
        self.lb.bind('<Double-Button-1>', self.copyToEntry)
    def copyToList(self, event):
        string = self.e.get()
        self.lb.insert(tk.END, string)
    def copyToEntry(self, event):
        index = self.lb.curselection()[0]
        string = self.lb.get(index)
        self.e.delete(0, tk.END)
        self.e.insert(tk.END, string)

def main():
    root = tk.Tk()
    win1 = windowTextList(root)
    root.mainloop()

if __name__ == '__main__':
    main()
