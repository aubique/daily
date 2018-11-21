#!/usr/bin/env python3
#p3_181119_1501.py
# Tkinter. Lesson 10.
# Canvas IDs, tags, animation

import tkinter as tk

INITIAL_COORDINATES = [0, 100, 40, 140]
STEP_DIVISION = 4

class AnimationWin():
    def __init__(self, master):
        self.master = master
        self.create_interface()
        self.pack_interface()
    def create_interface(self):
        self.c = tk.Canvas(self.master, width=300, height=200, bg='white')
        self.ball = self.c.create_oval(INITIAL_COORDINATES, fill='green')
    def pack_interface(self):
        self.c.pack()
        self.c.bind('<Button-3>', self.get_mouse_coords)
        self.c.bind('<Button-1>', self.mouse_handler)
        self.set_center_adjunction(self.ball)
    def set_center_adjunction(self, obj):
        coords = self.c.coords(obj)
        self.x_center = (coords[2] - coords[0]) / 2
        self.y_center = (coords[3] - coords[1]) / 2
    def mouse_handler(self, event):
        x_dest, y_dest = event.x - self.x_center, event.y - self.y_center
        x_init, y_init = self.c.coords(self.ball)[0:2]
        x_step = (x_dest - x_init) / STEP_DIVISION
        y_step = (y_dest - y_init) / STEP_DIVISION
        print("init: {}(x),{}(y)\nstep: {}(x),{}(y)\ndest: {}(x),{}(y)\n".format(
            x_init, y_init, x_step, y_step, x_dest, y_dest))
        self.motion(x_step, y_step)
    def motion(self, x, y):
        self.c.move(self.ball, x, y)
    def get_mouse_coords(self, event):
        x, y = event.x, event.y
        print(x, y)

def main():
    root = tk.Tk()
    win = AnimationWin(root)
    root.mainloop()

if __name__ == '__main__':
    main()
