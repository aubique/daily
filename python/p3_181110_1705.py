#!/usr/bin/env python3
#p3_181110_1705.py
# Tkinter. Lesson 6
# Listboxes

import tkinter as tk
PRODUCTS_LIST = [
    'apple', 'bananas', 'carrot', 'bread',
    'butter', 'meat', 'milk', 'potato', 'pineapple'
]

class toBuyList:
    def __init__(self, master):
        self.centerFrame = tk.Frame(master)
        self.createInterface(master)
        self.packInterface()
        self.fillItems()
    def createInterface(self, master):
        self.leftLBox = tk.Listbox(master, selectmode=tk.EXTENDED)
        self.rightLBox = tk.Listbox(master, selectmode=tk.EXTENDED)
        self.bAdd = tk.Button(self.centerFrame, text='>>>', command=self.funcAdd)
        self.bDel = tk.Button(self.centerFrame, text='<<<', command=self.funcDel)
    def packInterface(self):
        self.leftLBox.pack(side=tk.LEFT)
        self.centerFrame.pack(side=tk.LEFT)
        self.rightLBox.pack(side=tk.LEFT)
        self.bAdd.pack(side=tk.TOP)
        self.bDel.pack(side=tk.TOP)
    def fillItems(self):
        for item in PRODUCTS_LIST:
            self.leftLBox.insert(tk.END, item)
    def funcAdd(self):
        self.transferMultipleItems(self.leftLBox, self.rightLBox)
    def funcDel(self):
        self.transferMultipleItems(self.rightLBox, self.leftLBox)
    def transferMultipleItems(self, boxFrom, boxTo):
        try:
            indexList = list(boxFrom.curselection())
            indexList.reverse()
            for index in indexList:
                item = boxFrom.get(index)
                boxFrom.delete(index)
                boxTo.insert(tk.END, item)
        except IndexError: print('Item is not selected')

def main():
    root = tk.Tk()
    win1 = toBuyList(root)
    root.mainloop()

if __name__ == '__main__':
    main()
