#!/usr/bin/env python3
#p3_190203_2257.py
# Calculator Example
# One-expression-calculator (not more than one)

import tkinter as tk
from tkinter import messagebox as mb

BTN_HEIGHT = 1
BTN_WIDTH = 7
ENTRY_TEXT = "The result"

class Calculator:
    def __init__(self, master):
        self.master = master
        self.entry_var = tk.StringVar()
        self.create_interface()
        self.grid_interface()
        self.master.title("Simple Calculator")
        self.entry_var.set(ENTRY_TEXT)
        self.num = []
    def create_interface(self):
        self.button1 = tk.Button(self.master, text=' 1 ',
                                height=BTN_HEIGHT, width=BTN_WIDTH,
                                 command=lambda: self.add_number(1))
        self.button2 = tk.Button(self.master, text=' 2 ',
                                height=BTN_HEIGHT, width=BTN_WIDTH,
                                  command=lambda: self.add_number(2))
        self.button3 = tk.Button(self.master, text=' 3 ',
                                height=BTN_HEIGHT, width=BTN_WIDTH,
                                 command=lambda: self.add_number(3))
        self.button4 = tk.Button(self.master, text=' 4 ',
                                height=BTN_HEIGHT, width=BTN_WIDTH,
                                 command=lambda: self.add_number(4))
        self.button5 = tk.Button(self.master, text=' 5 ',
                                height=BTN_HEIGHT, width=BTN_WIDTH,
                                 command=lambda: self.add_number(5))
        self.button6 = tk.Button(self.master, text=' 6 ',
                                height=BTN_HEIGHT, width=BTN_WIDTH,
                                 command=lambda: self.add_number(6))
        self.button7 = tk.Button(self.master, text=' 7 ',
                                height=BTN_HEIGHT, width=BTN_WIDTH,
                                 command=lambda: self.add_number(7))
        self.button8 = tk.Button(self.master, text=' 8 ',
                                height=BTN_HEIGHT, width=BTN_WIDTH,
                                 command=lambda: self.add_number(8))
        self.button9 = tk.Button(self.master, text=' 9 ',
                                height=BTN_HEIGHT, width=BTN_WIDTH,
                                 command=lambda: self.add_number(9))
        self.button0 = tk.Button(self.master, text=' 0 ',
                                height=BTN_HEIGHT, width=BTN_WIDTH,
                                 command=lambda: self.add_number(0))
        self.button_divide = tk.Button(self.master, text=' / ',
                                      height=BTN_HEIGHT, width=BTN_WIDTH,
                                       lambda: set_action('/'))
        self.button_multiply = tk.Button(self.master, text=' x ',
                                        height=BTN_HEIGHT, width=BTN_WIDTH,
                                         lambda: set_action('*'))
        self.button_minus = tk.Button(self.master, text=' - ',
                                     height=BTN_HEIGHT, width=BTN_WIDTH,
                                      lambda: set_action('-'))
        self.button_plus = tk.Button(self.master, text=' + ',
                                    height=BTN_HEIGHT, width=BTN_WIDTH,
                                     lambda: set_action('+'))
        self.button_point = tk.Button(self.master, text=' . ',
                                     height=BTN_HEIGHT, width=BTN_WIDTH)
        self.button_clear = tk.Button(self.master, text='cls',
                                     height=BTN_HEIGHT, width=BTN_WIDTH)
        self.button_result = tk.Button(self.master, text='Enter',
                                       height=BTN_HEIGHT, width=BTN_WIDTH*5,
                                       command = self.show_result)
        self.entry_expression = tk.Entry(self.master, textvariable=self.entry_var,
                                         state='readonly', width=BTN_WIDTH*5)
    def grid_interface(self):
        self.entry_expression.grid(row=0, column=0, columnspan=4)
        self.button7.grid(row=1, column=0)
        self.button8.grid(row=1, column=1)
        self.button9.grid(row=1, column=2)
        self.button_divide.grid(row=1, column=3)
        self.button4.grid(row=2, column=0)
        self.button5.grid(row=2, column=1)
        self.button6.grid(row=2, column=2)
        self.button_multiply.grid(row=2, column=3)
        self.button1.grid(row=3, column=0)
        self.button2.grid(row=3, column=1)
        self.button3.grid(row=3, column=2)
        self.button_minus.grid(row=3, column=3)
        self.button_point.grid(row=4, column=0)
        self.button0.grid(row=4, column=1)
        self.button_clear.grid(row=4, column=2)
        self.button_plus.grid(row=4, column=3)
        self.button_result.grid(row=5, column=0, columnspan=4)
    def add_number(self, num):
        self.num.append(num)
    def show_result(self):
        self.number2 = self.num
        result_text = ' = ' + self.calculate()
        self.entry_expression.insert(tk.END, result_text)
        #mb.showinfo(None, self.num)
    def set_action(self, action):
        self.number1 = self.num
        self.num = ''
        self.set_entry(action)
    def set_entry(self, symbol):
        if self.entry_expression == ENTRY_TEXT:
            self.entry_expression.delete(0, tk.END)
        self.entry_expression.insert(tk.END, symbol)
    def calculate(self):
        pass

def main():
    root = tk.Tk()
    win = Calculator(root)
    root.mainloop()

if __name__ == '__main__':
    main()
