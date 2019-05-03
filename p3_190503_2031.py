#!/usr/bin/env python3
# p3_190503_2031.py
# SQLite exercise following a youTube lesson
# Complete Overview - Creating a Database, Table, and Running Queries
# https://www.youtube.com/watch?v=pd-0G0MigUA

import sqlite3

class Employee:
    """Sample Employee class"""

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
    @property
    def email(self):
        return '{}.{}@gmail.com'.format(self.first, self.last)
    @property
    def fullname(self):
        return '{} {}'.format(self.first, self.last)
    def __repr__(self):
        return "Employee('{}', '{}', '{})".format(
            self.first, self.last, self.pay
        )

def class_formatting():
    # c.execute("INSERT INTO employees VALUES ('{}', '{}', '{}')".format(
    #    emp1.first, emp1.last, emp1.pay))
    c.execute(
        "INSERT INTO employees VALUES (?, ?, ?)",
        (emp1.first, emp1.last, emp1.pay),
    )
    c.execute(
        "INSERT INTO employees VALUE (:first, :last, :pay)",
        {'first': emp2.first, 'last': emp2.last, 'pay': emp2.pay},
    )
    conn.commit()
    c.execute("SELECT * FROM employees WHERE last=?", ('Schafer',))
    print(c.fetchall())
    c.execute(
        "SELECT * FROM employees WHERE last=:last", {'last': 'Doe'}
    )
    print(c.fetchall())
    conn.commit()

def stream_formatting():
    c.execute(
        "INSERT INTO employees VALUES ('Annie', 'Schafer', 60000)"
    )
    conn.commit()
    c.execute("SELECT * FROM employees WHERE last='Schafer'")
    # c.fetchone()
    # c.fetchmany(5)
    print(c.fetchall())
    conn.commit()

def insert_emp(emp):
    with conn:
        c.execute(
            "INSERT INTO employees VALUES (:first, :last, :pay)",
            {'first': emp.first, 'last': emp.last, 'pay': emp.pay},
        )

def get_emps_by_name(lastname):
    c.execute(
        "SELECT * FROM employees WHERE last=:last", {'last': lastname}
    )
    return c.fetchall()

def update_pay(emp, pay):
    with conn:
        c.execute(
            """UPDATE employees SET pay = :pay
                  WHERE first = :first and last = :last""",
            {'first': emp.first, 'last': emp.last, 'pay': pay},
        )

def remove_emp(emp):
    with conn:
        c.execute(
            "DELETE from employees WHERE first = :first AND last = :last",
            {'first': emp.first, 'last': emp.last},
        )

def main():
    pass

if __name__ == '__main__':
    emp1 = Employee('John', 'Doe', 80000)
    emp2 = Employee('Jane', 'Doe', 90000)
    # conn = sqlite3.connect('files/p3_190503_2031.db')
    conn = sqlite3.connect(':memory:')
    c = conn.cursor()
    c.execute(
        """CREATE TABLE employees (
        first text,
        last text,
        pay integer
    )"""
    )

    # stream_formatting()
    # class_formatting()
    insert_emp(emp1)
    insert_emp(emp2)
    emps = get_emps_by_name('Doe')
    print(emps)
    update_pay(emp2, 95000)
    remove_emp(emp1)
    emps = get_emps_by_name('Doe')
    print(emps)

    conn.close()
