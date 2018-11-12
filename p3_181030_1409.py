#!/usr/bin/env python3
#p3_181030_1409.py
# Text Editor Example
# Lesson 4 [tkinter]: Text

import tkinter as tk

class TextWindow():
    def __init__(self, master):
        self.f_top = tk.Frame(master)
        self.f_bot = tk.Frame(master)
        self.t = tk.Text(self.f_top, width=25, height=5)
        self.s = tk.Scrollbar(self.f_top, command=self.t.yview)
        self.b_insert = tk.Button(self.f_bot, text='Вставить',
                                command=self.insertText)
        self.b_get = tk.Button(self.f_bot, text='Взять', command=self.getText)
        self.b_delete = tk.Button(self.f_bot, text='Удалить', command=self.deleteText)
        self.l = tk.Label(master)
        self.packupInterface()
    def packupInterface(self):
        self.f_top.pack()
        self.f_bot.pack()
        self.t.pack(side=tk.LEFT)
        self.s.pack(side=tk.LEFT, fill=tk.Y)
        self.t.config(yscrollcommand=self.s.set)
        self.b_insert.pack(side=tk.LEFT)
        self.b_get.pack(side=tk.LEFT)
        self.b_delete.pack(side=tk.LEFT)
        self.l.pack()
    def insertText(self):
        string = "Hello World!"
        self.t.insert(1.0, string)
    def getText(self):
        string = self.t.get(1.0, tk.END)
        self.l.config(text=string)
    def deleteText(self):
        self.t.delete(1.0, tk.END)

def main():
    root = tk.Tk()
    win1 = TextWindow(root)
    root.tk.mainloop()

if __name__ == '__main__':
    main()
