# import sqlite3
# import os

# PATH = os.path.abspath(__file__+"/../")
# FILE_PATH = PATH +"/BD.sqlite3"

# db = sqlite3.connect(FILE_PATH)

# def create_table():
#     QUERY = '''
#     CREATE TABLE IF NOT EXISTS costs(
#     id INTEGER PRIMARY KEY AUTOINCREMENT,
#     appointment VARCHAR(255),
#     price INTEGER NOT NULL,
#     date DATATIME NOT NULL DEFAULT CURRENT_TIMESTAMP
#     );
#     '''
#     db.execute(QUERY)

# def add_costs(type="expense"):
#     appointment = input("enter appointment :")
#     price = input("enter price :")

#     QUERY = '''
#     INSERT INTO costs (appointment, price,type) VALUES (?,?,?)
#     ;'''
#     db.execute(QUERY,[appointment,price,type])
#     db.commit()
# def count_income():   
#     QUERY = '''
#     SELECT SUM(price)  FROM costs WHERE type="expense"
#     '''
#     rez = db.execute(QUERY)
#     return rez.fetchall()

# def count_expense():
#     QUERY = '''
#     SELECT SUM(price)  FROM costs WHERE type="income"
#     '''
#     rez = db.execute(QUERY)
#     return rez.fetchall()
# # create_table()

# # db.execute('''
# # ALTER TABLE costs ADD COLUMN type TEXT DEFAULT 'expense';
# # ''')
# # db.commit()

# print(count_income())



import sqlite3
import os
import requests

URL = "https://api.monobank.ua/bank/currency"

PATH = os.path.abspath(__file__+"/../")
FILE_PATH = PATH +"/BD.sqlite3"

db = sqlite3.connect(FILE_PATH)

def create_table():
    QUERY = '''
    CREATE TABLE IF NOT EXISTS exchange(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    currency_id INTEGER NOT NULL,
    currency_name VARCHAR(255),
    currency_value REAL NOT NULL
    );
    '''
    db.execute(QUERY)

# response = requests.request("get", URL)

def add_exchence(currency_name:int, value:int):
     QUERY = '''
    INSERT INTO exchange (currency_id, currency_value) 
    VALUES (?,?);
    '''
     db.execute(QUERY,[currency_name,value])

def write_in_table():
        response = requests.request("get", URL)
        datas = response.json()
        print(response.status_code)
        for data in datas:
            if(data["currencyCodeB"] == 980):
                try:
                    currency_id = data["currencyCodeA"]
                    currency_value = data["rateBuy"]
                    add_exchence(currency_id,currency_value)
                    print("AA ")

                except KeyError:
                    pass
            db.commit()

            # try:
            #     print(data["rateCross"])
            # except KeyError:
            #      pass
            


write_in_table()
# db.execute('''
# DROP TABLE exchange
# ''')


                

