#!/usr/bin/env python3
#p3_190203_2257.py
# Calculator Example
# One-expression-calculator (not more than one)

import tkinter as tk
from tkinter import messagebox as mb

BTN_HEIGHT = 1
BTN_WIDTH = 7
ENTRY_TEXT = "Press buttons to get an expression"

class Calculator:
    def __init__(self, master):
        self.master = master
        self.entry_data = tk.StringVar()
        self.create_interface()
        self.grid_interface()
        # Variables assignment
        self.master.title("Simple Calculator")
        self.entry_data.set(ENTRY_TEXT)
        self.expression = ''
        self.is_result = False
    def create_interface(self):
        self.button1 = tk.Button(self.master, text=' 1 ',
                                height=BTN_HEIGHT, width=BTN_WIDTH,
                                 command=lambda: self.press(1))
        self.button2 = tk.Button(self.master, text=' 2 ',
                                height=BTN_HEIGHT, width=BTN_WIDTH,
                                  command=lambda: self.press(2))
        self.button3 = tk.Button(self.master, text=' 3 ',
                                height=BTN_HEIGHT, width=BTN_WIDTH,
                                 command=lambda: self.press(3))
        self.button4 = tk.Button(self.master, text=' 4 ',
                                height=BTN_HEIGHT, width=BTN_WIDTH,
                                 command=lambda: self.press(4))
        self.button5 = tk.Button(self.master, text=' 5 ',
                                height=BTN_HEIGHT, width=BTN_WIDTH,
                                 command=lambda: self.press(5))
        self.button6 = tk.Button(self.master, text=' 6 ',
                                height=BTN_HEIGHT, width=BTN_WIDTH,
                                 command=lambda: self.press(6))
        self.button7 = tk.Button(self.master, text=' 7 ',
                                height=BTN_HEIGHT, width=BTN_WIDTH,
                                 command=lambda: self.press(7))
        self.button8 = tk.Button(self.master, text=' 8 ',
                                height=BTN_HEIGHT, width=BTN_WIDTH,
                                 command=lambda: self.press(8))
        self.button9 = tk.Button(self.master, text=' 9 ',
                                height=BTN_HEIGHT, width=BTN_WIDTH,
                                 command=lambda: self.press(9))
        self.button0 = tk.Button(self.master, text=' 0 ',
                                height=BTN_HEIGHT, width=BTN_WIDTH,
                                 command=lambda: self.press(0))
        self.button_divide = tk.Button(self.master, text=' / ',
                                      height=BTN_HEIGHT, width=BTN_WIDTH,
                                       command=lambda: self.press('/'))
        self.button_multiply = tk.Button(self.master, text=' x ',
                                        height=BTN_HEIGHT, width=BTN_WIDTH,
                                         command=lambda: self.press('*'))
        self.button_minus = tk.Button(self.master, text=' - ',
                                     height=BTN_HEIGHT, width=BTN_WIDTH,
                                      command=lambda: self.press('-'))
        self.button_plus = tk.Button(self.master, text=' + ',
                                    height=BTN_HEIGHT, width=BTN_WIDTH,
                                     command=lambda: self.press('+'))
        self.button_point = tk.Button(self.master, text=' . ',
                                     height=BTN_HEIGHT, width=BTN_WIDTH,
                                      command=lambda: self.press('.'))
        self.button_clear = tk.Button(self.master, text='cls',
                                     height=BTN_HEIGHT, width=BTN_WIDTH,
                                      command=self.do_clear)
        self.button_result = tk.Button(self.master, text='Enter',
                                       height=BTN_HEIGHT, width=BTN_WIDTH*5,
                                       command=self.calculate_result)
        self.entry_field = tk.Entry(self.master, textvariable=self.entry_data,
                                         state='readonly', width=BTN_WIDTH*5)
    def grid_interface(self):
        self.entry_field.grid(row=0, column=0, columnspan=4)
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
    def press(self, num):
        if self.verify_not_operand(num) and self.is_result:
            self.expression = ''
        self.expression = self.expression + str(num)
        self.entry_data.set(self.expression)
        self.is_result = False
    def calculate_result(self):
        try:
            self.expression = str(eval(self.entry_data.get()))
            self.entry_data.set(self.expression)
            self.is_result = True
        except Exception as error_type:
            print('Error info:', error_type)
            self.entry_data.set('Error occured')
            self.expression = ''
    def do_clear(self):
        self.expression = self.entry_data.get()[:-1]
        self.entry_data.set(self.expression)
    def verify_not_operand(self, operand):
        if not operand in ('+', '-', '*', '/'): return True
        else: return False

def main():
    root = tk.Tk()
    win = Calculator(root)
    root.mainloop()

if __name__ == '__main__':
    main()
