#!/usr/bin/env python3
<<<<<<< HEAD
#p3_181125_2224.py
# Tkinter. Lesson 14.
# Widget Menu
=======
#p3_181121_2116.py
# Tkinter. Lesson 13.
# Filedialogs
>>>>>>> origin/master

import tkinter as tk
from tkinter import filedialog as fd
from tkinter import messagebox as mb

class OpenSaveFile:
    def __init__(self, master):
        self.master = master
        self.create_interface()
        self.pack_interface()
    def create_interface(self):
        self.text = tk.Text(width=50, height=25)
        self.b1 = tk.Button(text='Open', command=self.insert_text)
        self.b2 = tk.Button(text='Save', command=self.extract_text)
        self.b3 = tk.Button(text='Clear', command=self.clear_text)
    def pack_interface(self):
        self.text.grid(columnspan=3)
        self.b1.grid(row=1)
        self.b2.grid(row=1, column=1)
        self.b3.grid(row=1, column=2)
    def insert_text(self):
        try:
            file_name = fd.askopenfilename()
            f = open(file_name)
            s = f.read()
            self.text.insert(1.0, s)
            f.close()
        except Exception as ex: self.exception_handler(ex)
    def extract_text(self):
        try:
            file_name = fd.asksaveasfilename(filetypes=(('TXT files', '*.txt'),
                ('HTML files', '*.html;*.htm'), ('All files', '*.*') ))
            f = open(file_name, 'w')
            s = self.text.get(1.0, tk.END)
            f.write(s)
            f.close()
        except Exception as ex: self.exception_handler(ex)
    def exception_handler(self, ex):
        if type(ex) == TypeError: self.display_error(ex, 'Wrong file chosen')
        elif type(ex) == FileNotFoundError: self.display_error(ex, 'Choose a file')
        else: self.display_error(0, 'Unknown Error')
    def display_error(self, exception, message):
        print("Error occured:", exception)
        mb.showerror('Error', message)
    def clear_text(self):
        result = mb.askyesno("Clear Text", "Do you want to clear all the text?")
        if result: self.text.delete(1.0, tk.END)

def main():
    root = tk.Tk()
    win = OpenSaveFile(root)
    root.mainloop()

if __name__ == '__main__':
    main()
