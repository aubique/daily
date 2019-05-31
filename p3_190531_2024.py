#!/usr/bin/env python3
# p3_190531_2024.py
# SQLite3 class for JWS script (p3_190528_2334.py)

import sqlite3

TABLE = "jws"
EVENT = "event_id"
DESC = "description"
DATE = "date"
LINK = "url_download"

class SQLighter:
    def __init__(self):
        self.conn = sqlite3.connect("files/p3_190531_2024.db")
        self.c = self.conn.cursor()
        self.new_table()
    def new_table(self):
        """Create a table if itsn't already existing"""
        self.c.execute(
            """CREATE TABLE IF NOT EXISTS {table} (
            id integer primary key,
            {event} integer,
            {desc} text,
            {date} text,
            {link} text)
            """.format(
                table=TABLE,
                event=EVENT,
                desc=DESC,
                date=DATE,
                link=LINK,
            )
        )
    def close(self):
        """Close this connection with DB"""
        self.conn.close()
    def select_all_rows(self):
        """Select all rows from the table"""
        with self.conn:
            self.c.execute("SELECT * FROM %s" % (TABLE))
            return self.c.fetchall()
    def count_rows(self):
        """Return a number of rows in the table"""
        with self.conn:
            return len(self.select_all_rows())
    def select_id(self, id):
        """Get one row by ID"""
        with self.conn:
            self.c.execute(
                """SELECT * FROM %s WHERE id = ?""" % (TABLE), (id,)
            )
            return self.c.fetchone()
    def select_event(self, event_id):
        """Search a row by event_ID"""
        with self.conn:
            self.c.execute(
                """SELECT * FROM {table} WHERE {event} = ?""".format(
                    table=TABLE, event=EVENT
                ),
                (event_id,),
            )
            return self.c.fetchone()
    def insert_row(self, event_id, description, date, link_url):
        """Add a row to the DB"""
        with self.conn:
            self.c.execute(
                """INSERT INTO {table}({event}, {desc}, {date}, {link})
                VALUES (?, ?, ?, ?)""".format(
                    table=TABLE,
                    event=EVENT,
                    desc=DESC,
                    date=DATE,
                    link=LINK,
                ),
                (event_id, description, date, link_url),
            )

def search_event(event_id):
    row = db.select_event(event_id)
    if row:
        return row
    else:
        return False

if __name__ == "__main__":
    db = SQLighter()
    print(db.count_rows())
    # print(db.select_id(1))
    print(
        db.insert_row(2, "test #2", "31-05-2019", "https://google.com")
    )
    print(search_event(2))
