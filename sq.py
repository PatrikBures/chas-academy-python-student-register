import sqlite3
from pathlib import Path

PATH = Path("db.sqlite3")
CON = None

def open():
    global CON
    CON = sqlite3.connect(PATH)
    
def close():
    if CON:
        CON.close()

def init_table():
    if not CON: return

    cur = CON.cursor()

    cur.execute("CREATE TABLE IF NOT EXISTS students(name, age, hobby)")

    CON.commit()

def add_student(name, age, hobby):
    if not CON: return

    cur = CON.cursor()

    data = (name, age, hobby)


    cur.execute(f"INSERT INTO students VALUES(?,?,?)", data)

    CON.commit()
    
def search_student(name_to_search):
    if not CON: return

    cur = CON.cursor()
    
    found_student = cur.execute(f"SELECT name, age, hobby FROM students WHERE name = '{name_to_search}';")
    
    return found_student

def get_all_students():
    if not CON: return

    cur = CON.cursor()

    students = cur.execute(f"SELECT name, age, hobby FROM students ORDER BY name")

    return students

