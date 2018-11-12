#!/usr/bin/env python3
#p3_181029_1723.py
# Frames VER.2
# Lesson 3: method pack()

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
        self.frameTop = self.frameBottom = tk.Frame(master)
        self.markupInterface(colors)
        self.packupInterface()
    def markupInterface(self, colors):
        self.l = tk.Label(self.frameTop, width=30)
        self.e = tk.Entry(self.frameTop, width=30, justify=tk.CENTER)
        self.b1 = tk.Button(self.frameBottom, width=1, bg=colors[RED],
                            command=lambda: self.fillLabels(RED))
        self.b2 = tk.Button(self.frameBottom, width=1, bg=colors[ORANGE],
                            command=lambda: self.fillLabels(ORANGE))
        self.b3 = tk.Button(self.frameBottom, width=1, bg=colors[YELLOW],
                            command=lambda: self.fillLabels(YELLOW))
        self.b4 = tk.Button(self.frameBottom, width=1, bg=colors[GREEN],
                            command=lambda: self.fillLabels(GREEN))
        self.b5 = tk.Button(self.frameBottom, width=1, bg=colors[CYAN],
                            command=lambda: self.fillLabels(CYAN))
        self.b6 = tk.Button(self.frameBottom, width=1, bg=colors[BLUE],
                            command=lambda: self.fillLabels(BLUE))
        self.b7 = tk.Button(self.frameBottom, width=1, bg=colors[PURPLE],
                            command=lambda: self.fillLabels(PURPLE))
    def packupInterface(self):
        self.l.pack(side=tk.TOP)
        self.e.pack(side=tk.TOP)
        self.b1.pack(side=tk.LEFT)
        self.b2.pack(side=tk.LEFT)
        self.b3.pack(side=tk.LEFT)
        self.b4.pack(side=tk.LEFT)
        self.b5.pack(side=tk.LEFT)
        self.b6.pack(side=tk.LEFT)
        self.b7.pack(side=tk.LEFT)
        self.frameTop.pack()
        self.frameBottom.pack()
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
