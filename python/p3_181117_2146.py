#!/usr/bin/env python3
#p3_181117_2146.py
# Tkinter. Lesson 9
# Canvas example

import tkinter as tk
INITIAL_COORDINATES = [0, 200, 10, 170]

class ImageWin:
    def __init__(self, master):
        self.create_interface(master)
        self.pack_interface()
    def create_interface(self, master):
        self.c = tk.Canvas(master, width=200, height=200, bg='white')
        self.c.create_polygon((100, 25), (25, 80), (50, 80), (50, 180),
                (150, 180), (150, 80), (175, 80), (100, 25), fill='cyan')
        self.c.create_oval(140, 10, 190, 60, fill='orange', outline='yellow')
        self.create_grass()
    def pack_interface(self):
        self.c.pack()
    def create_grass(self):
        x0y0x1y1_coords = INITIAL_COORDINATES
        # While x0 is within 200x size of window
        while x0y0x1y1_coords[0] < 200:
            self.c.create_line(x0y0x1y1_coords, fill='green', width=2)
            new_list = list()
            index = 1
            for coordinate in x0y0x1y1_coords:
                new_coord = coordinate
                # If index of coordinate list is even, we take only x0 and x1 coords
                if index % 2:
                    new_coord += 10
                # Add a new coordinate to the new list and replace the old one to move on
                new_list.append(new_coord)
                index += 1
            x0y0x1y1_coords = new_list

def main():
    root = tk.Tk()
    win = ImageWin(root)
    root.mainloop()

if __name__ == '__main__':
    main()
