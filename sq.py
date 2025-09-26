import sqlite3
from pathlib import Path

PATH = Path("db.sqlite3")

def init_table():
    if PATH.exists():
        return

    con = sqlite3.connect(PATH)
    cur = con.cursor()

    cur.execute("CREATE TABLE students(name, age, hobby)")

    con.commit()
    con.close()
