#!/usr/bin/env python3
#p3_181030_1451.py
# Simple Text Editor with open-save functionality

import tkinter as tk
FOLDER_PATH = 'files/'

class TextEditor:
    def __init__(self, master):
        self.f_top = tk.Frame(master)
        self.f_cen = tk.Frame(master)
        self.f_bot = tk.Frame(master)
        self.e = tk.Entry(self.f_top, width=20)
        self.b_open = tk.Button(self.f_top, text="Открыть",
                                command=self.readFile)
        self.b_save = tk.Button(self.f_top, text="Сохранить",
                                command=self.saveFile)
        self.t = tk.Text(self.f_cen, width=40, height=10)
        self.sy = tk.Scrollbar(self.f_cen, command=self.t.yview)
        self.sx = tk.Scrollbar(self.f_cen, orient=tk.HORIZONTAL, command=self.t.xview)
        self.packInterface()
    def packInterface(self):
        self.f_top.pack(side=tk.TOP)
        self.f_cen.pack(side=tk.TOP)
        self.f_bot.pack(side=tk.TOP)

        self.e.pack(side=tk.LEFT)
        self.b_open.pack(side=tk.LEFT)
        self.b_save.pack(side=tk.LEFT)
        self.sy.pack(side=tk.RIGHT, fill=tk.Y)
        self.sx.pack(side=tk.BOTTOM, fill=tk.X)
        self.t.pack()
        self.t.config(yscrollcommand=self.sy.set, xscrollcommand=self.sx.set)
    def openFile(self):
        fullPath = FOLDER_PATH + self.e.get()
        return fullPath
    def readFile(self):
        self.fileToRead = open(self.openFile(), 'rt')
        fileData = self.fileToRead.read()[:-1]
        self.t.delete(1.0, tk.END)
        self.t.insert(1.0, fileData)
        if self.fileToRead: self.fileToRead.close()
    def saveFile(self):
        self.fileToWrite = open(self.openFile(), 'wt')
        fileData = self.t.get(1.0, tk.END)
        self.fileToWrite.write(fileData)
        if self.fileToWrite: self.fileToWrite.close()

def main():
    root = tk.Tk()
    win1 = TextEditor(root)
    root.tk.mainloop()

if __name__ == '__main__':
    main()
