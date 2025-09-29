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

def add_student(name, age, hobby):
    con = sqlite3.connect(PATH)
    cur = con.cursor()

    data = (name, age, hobby)


    cur.execute(f"INSERT INTO students VALUES(?,?,?)", data)

    con.commit()
    con.close()

def get_all_students():
    con = sqlite3.connect(PATH)
    cur = con.cursor()

    students = cur.execute(f"SELECT name, age, hobby FROM students ORDER BY name")
    return students

