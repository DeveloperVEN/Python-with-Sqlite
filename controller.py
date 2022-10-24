from asyncio import streams
import os
import sqlite3 as sql

db_name = 'streamers.db'

db_is_new = not os.path.exists(db_name)

conn = sql.connect(db_name)

if db_is_new:
    print('Need to create schema')
else:
    print('Database exists, assume schema does, too.')

conn.close() 


def createTable():
    conn = sql.connect("streamers.db")
    cursor = conn.cursor()
    cursor.execute(
        """CREATE TABLE streamers (
            name text,
            followers integer,
            subs integer
        )"""
    )
    conn.commit()
    conn.close() 


def insertRows(nombre, followers, subs):
    conn  = sql.connect("streamers.db")
    cursor = conn.cursor()
    instruction = f"INSERT INTO streamers VALUES ('{nombre}', {followers}, {subs})"
    cursor.execute(instruction)

    conn.commit() 
    conn.close()  


def readRows(nombre, followers, subs):
    conn  = sql.connect("streamers.db")
    cursor = conn.cursor()
    instruction = f"SELECT * FROM streamers"
    cursor.execute(instruction)
    datos = cursor.fetchall()

    conn.commit() 
    conn.close()
    print(datos) 

def insertRows(streamersList):
    conn  = sql.connect("streamers.db")
    cursor = conn.cursor()
    instruction = f"INSERT INTO streamers VALUES (?, ?, ?)"
    cursor.executemany(instruction, streamersList)

    conn.commit() 
    conn.close()  


def readOrdered(field):
    conn  = sql.connect("streamers.db")
    cursor = conn.cursor()
    instruction = f"SELECT * FROM streamers ORDER BY {field} DESC"
    cursor.execute(instruction)
    datos = cursor.fetchall()

    conn.commit() 
    conn.close()
    print(datos) 

def search():
    conn  = sql.connect("streamers.db")
    cursor = conn.cursor()
    instruction = f"SELECT * FROM streamers WHERE name = 'mi Mami'"
    cursor.execute(instruction)
    datos = cursor.fetchall()

    conn.commit() 
    conn.close()
    print(datos) 


def updateField():
    conn  = sql.connect("streamers.db")
    cursor = conn.cursor()
    instruction = f"UPDATE streamers SET followers=12000000 WHERE name like 'ibai'" 
    cursor.execute(instruction)
    
    conn.commit() 
    conn.close()
    
def deleteRow():
    conn  = sql.connect("streamers.db")
    cursor = conn.cursor()
    instruction = f"DELETE FROM streamers WHERE name like 'ibai'" 
    cursor.execute(instruction)
    
    conn.commit() 
    conn.close()


if __name__ == "__main__":
    #createDB()
    #createTable()
    #insertRow("Ibai",7000000,25000)
    #insertRow("Willber", 8000000, 1000000)
    #readRows() 
    streamers = [ 
        ("Willsy", 9000000, 8000000),
        ("willinger", 5000000, 9000000),
        ("mi Mami", 10000000000, 8000000),
        ("el Viejo", 12000000, 4000000),
        ("YO",5000000,6000000)
    ]
    #insertRows(streamers)
    #readRows()
    #readOrdered("subs")
    #search()
    #updateField()
    deleteRow()







