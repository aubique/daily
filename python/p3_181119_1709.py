#!/usr/bin/env python3
#p3_181119_1709.py
# Tkinter. Lesson 11.
# Windows

import tkinter as tk

class MainWindow:
    def __init__(self, master):
        self.master = master
        self.figure = tk.StringVar()
        self.create_window1()
        self.aux = None
    def create_window1(self):
        self.master.title('Main Menu')
        self.c = tk.Canvas(self.master, width=400, height=350, bg='white')
        self.btn_add = tk.Button(self.master, width=200, height=50,
                text='Add a form', command=self.add_form)
        self.master.geometry('400x400+340+150')
        self.c.pack()
        self.btn_add.pack()
    def create_window2(self):
        if self.aux: self.aux.destroy()
        self.aux = tk.Toplevel()
        self.aux.title('Setting coordinates')
        self.lbl_x1 = tk.Label(self.aux, text='x1')
        self.lbl_x2 = tk.Label(self.aux, text='x2')
        self.lbl_y1 = tk.Label(self.aux, text='y1')
        self.lbl_y2 = tk.Label(self.aux, text='y2')
        self.txt_x1 = tk.Entry(self.aux, width=15)
        self.txt_x2 = tk.Entry(self.aux, width=15)
        self.txt_y1 = tk.Entry(self.aux, width=15)
        self.txt_y2 = tk.Entry(self.aux, width=15)
        self.rdo_1 = tk.Radiobutton(self.aux, text='rectangle',
                variable=self.figure, value='rect')
        self.rdo_2 = tk.Radiobutton(self.aux, text='oval',
                variable=self.figure, value='oval')
        self.btn_draw = tk.Button(self.aux, text='Draw', width=20, command=self.draw_form)
    def pack_window2(self):
        self.aux.geometry('300x150+750+300')
        self.lbl_x1.grid(row=0, column=0)
        self.lbl_x2.grid(row=1, column=0)
        self.txt_x1.grid(row=0, column=1)
        self.txt_x2.grid(row=1, column=1)
        self.lbl_y1.grid(row=0, column=2)
        self.lbl_y2.grid(row=1, column=2)
        self.txt_y1.grid(row=0, column=3)
        self.txt_y2.grid(row=1, column=3)
        self.rdo_1.grid(row=2, column=1, rowspan=2, columnspan=4, sticky=tk.W)
        self.rdo_2.grid(row=4, column=1, rowspan=2, columnspan=4, sticky=tk.W)
        self.btn_draw.grid(row=6, column=1, columnspan=4, pady=10)
    def add_form(self):
        self.create_window2()
        self.pack_window2()
    def get_coords(self):
        x1 = self.txt_x1.get()
        x2 = self.txt_x2.get()
        y1 = self.txt_y1.get()
        y2 = self.txt_y2.get()
        return x1, x2, y1, y2
    def draw_form(self):
        x1, x2, y1, y2 = self.get_coords()
        if self.figure.get() == 'rect':
            self.draw_rect(x1, x2, y1, y2)
        elif self.figure.get() == 'oval':
            self.draw_oval(x1, x2, y1, y2)
    def draw_rect(self, x1, x2, y1, y2):
        self.c.create_rectangle(x1, x2, y1, y2, width=3)
    def draw_oval(self, x1, x2, y1, y2):
        self.c.create_oval(x1, x2, y1, y2, width=3)

def main():
    root = tk.Tk()
    win1 = MainWindow(root)
    root.mainloop()

if __name__ == '__main__':
    main()
