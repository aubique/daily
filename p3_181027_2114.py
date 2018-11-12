#!/usr/bin/env python3
#p3_181027_2114.py
# Color-app
# Lesson 2: Widgets

import tkinter as tk
RED     = "red"
ORANGE  = "orange"
YELLOW  = "yellow"
GREEN   = "green"
CYAN    = "cyan"
BLUE    = "blue"
PURPLE  = "purple"

class Instance:
    def __init__(self, master):
        colors = self.getColorDictionary()
        self.markupInterface(master, colors)
        self.packupInterface()
    def markupInterface(self, master, colors):
        self.l = tk.Label(master, width=13)
        self.e = tk.Entry(master, width=13, justify=tk.CENTER)
        self.b1 = tk.Button(master, width=10, bg=colors[RED],
                            command=lambda: self.fillLabels(RED))
        self.b2 = tk.Button(master, width=10, bg=colors[ORANGE],
                            command=lambda: self.fillLabels(ORANGE))
        self.b3 = tk.Button(master, width=10, bg=colors[YELLOW],
                            command=lambda: self.fillLabels(YELLOW))
        self.b4 = tk.Button(master, width=10, bg=colors[GREEN],
                            command=lambda: self.fillLabels(GREEN))
        self.b5 = tk.Button(master, width=10, bg=colors[CYAN],
                            command=lambda: self.fillLabels(CYAN))
        self.b6 = tk.Button(master, width=10, bg=colors[BLUE],
                            command=lambda: self.fillLabels(BLUE))
        self.b7 = tk.Button(master, width=10, bg=colors[PURPLE],
                            command=lambda: self.fillLabels(PURPLE))
    def packupInterface(self):
        self.l.pack()
        self.e.pack()
        self.b1.pack()
        self.b2.pack()
        self.b3.pack()
        self.b4.pack()
        self.b5.pack()
        self.b6.pack()
        self.b7.pack()
    def getColorDictionary(self):
        nameOfColors = [RED, ORANGE, YELLOW, GREEN, CYAN, BLUE, PURPLE]
        codeOfColors = ["#ff0000", "#ff7d00", "#ffff00",
                        "#00ff00", "#007dff", "#0000ff", "#7d00ff"]
        return dict(zip(nameOfColors, codeOfColors))
    def fillLabels(self, color):
        self.l.config(text=color)
        self.e.delete(0, tk.END)
        self.e.insert(0, self.getColorDictionary()[color])

def main():
    root = tk.Tk()
    window = Instance(root)
    root.tk.mainloop()

if __name__ == '__main__':
    main()
