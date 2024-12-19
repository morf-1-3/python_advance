import sqlite3
import os

PATH = os.path.abspath(__file__+"/../")
FILE_PATH = PATH +"/BD.sqlite3"

db = sqlite3.connect(FILE_PATH)

def create_table():
    query = '''CREATE TABLE IF NOT EXISTS worker(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name VARCHAR(255) NOT NULL,
    lastName VARCHAR(255) NOT NULL,
    selery INTEGER NOT NULL,
    conversion INTEGER NOT NULL
    );'''
    db.execute(query)

def add_worker(name:str, last_name:str, selery:int, conversion:int):
    query = '''
    INSERT INTO worker (name,lastname,selery,conversion) VALUES (?,?,?,?);
    '''
    db.execute(query,[name,last_name,selery,conversion])
    db.commit()

def delete_by_id(id:int):
    query = '''
    DELETE FROM worker where id = ?
    '''
    db.execute(query,[id])
    db.commit()

def get_all():
    query = '''
    SELECT name, lastname, id FROM worker
    '''
    rezult = db.execute(query)
    return rezult

def get_selery():
    query = '''
    SELECT selery + selery*0.1 FROM worker where conversion > 0.5
    '''
    second_query = '''
    SELECT selery  FROM worker where conversion <= 0.5
    '''
    rezult = list(db.execute(query))
    rezult += list(db.execute(second_query))
    return rezult

def find_lastname(lastname:str):
    query = '''
    SELECT name, lastname, id FROM worker where lastname like ?
    '''
    lastname = f"%{lastname}%"
    rezult = db.execute(query,[lastname])
    return rezult

rez = (find_lastname("qw").fetchall())
print(rez)