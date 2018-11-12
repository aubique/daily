#!/usr/bin/env python3
#p3_181029_1647.py
# Frames
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
    def __init__(self, frame1, frame2):
        colors = self.getColorDictionary()
        self.markupInterface(frame1, frame2, colors)
        self.packupInterface(frame1, frame2)
    def markupInterface(self, f_top, f_bot, colors):
        self.l = tk.Label(f_top, width=30)
        self.e = tk.Entry(f_top, width=30, justify=tk.CENTER)
        self.b1 = tk.Button(f_bot, width=1, bg=colors[RED],
                            command=lambda: self.fillLabels(RED))
        self.b2 = tk.Button(f_bot, width=1, bg=colors[ORANGE],
                            command=lambda: self.fillLabels(ORANGE))
        self.b3 = tk.Button(f_bot, width=1, bg=colors[YELLOW],
                            command=lambda: self.fillLabels(YELLOW))
        self.b4 = tk.Button(f_bot, width=1, bg=colors[GREEN],
                            command=lambda: self.fillLabels(GREEN))
        self.b5 = tk.Button(f_bot, width=1, bg=colors[CYAN],
                            command=lambda: self.fillLabels(CYAN))
        self.b6 = tk.Button(f_bot, width=1, bg=colors[BLUE],
                            command=lambda: self.fillLabels(BLUE))
        self.b7 = tk.Button(f_bot, width=1, bg=colors[PURPLE],
                            command=lambda: self.fillLabels(PURPLE))
    def packupInterface(self, f_top, f_bot):
        self.l.pack(side=tk.TOP)
        self.e.pack(side=tk.TOP)
        self.b1.pack(side=tk.LEFT)
        self.b2.pack(side=tk.LEFT)
        self.b3.pack(side=tk.LEFT)
        self.b4.pack(side=tk.LEFT)
        self.b5.pack(side=tk.LEFT)
        self.b6.pack(side=tk.LEFT)
        self.b7.pack(side=tk.LEFT)
        f_top.pack()
        f_bot.pack()
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
    frameTop = frameBottom = tk.Frame(root)
    window = Instance(frameTop, frameBottom)
    root.tk.mainloop()

if __name__ == '__main__':
    main()
