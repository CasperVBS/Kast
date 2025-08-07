import sqlite3
import os

os.makedirs("database",exist_ok=True)

pad_db = os.path.join("database","Database_kast.db")
pad_sql = os.path.join("database","schema.sql")

with open(pad_sql, "r", encoding="utf-8") as f:
    sql_script = f.read()

conn = sqlite3.connect(pad_db)
cursor = conn.cursor()

cursor.executescript(sql_script)

conn.commit()

def new_item(item,X,Y,img):
    conn = sqlite3.connect(pad_db)
    cursor = conn.cursor()
    nieuw_item = (item,X,Y,img)
    cursor.execute("INSERT OR IGNORE INTO kast_stock (item, x,y,img) VALUES (?, ?,?,?)", nieuw_item)
    conn.commit()

def lijst_items():
    pad_db = os.path.join("database","Database_kast.db")    
    conn = sqlite3.connect(pad_db)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM kast_stock")
    arr = []
    for rij in cursor.fetchall():
        arr.append(rij[1])
    print(arr)
    return arr

def lijst_img():
    pad_db = os.path.join("database","Database_kast.db")
    conn = sqlite3.connect(pad_db)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM kast_stock")
    arr = []
    for rij in cursor.fetchall():
        arr.append(rij[4])
    return arr




def clear():
    conn = sqlite3.connect("database/Database_kast.db")
    cursor = conn.cursor()

    cursor.execute("DELETE FROM kast_stock")  
    conn.commit()
    conn.close()
