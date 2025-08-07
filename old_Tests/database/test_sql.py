import sqlite3
import os

# Zorg dat de map 'database' bestaat
os.makedirs("database", exist_ok=True)

# Pad naar de database
pad_naar_db = os.path.join("database", "mijn_database.db")

# Pad naar het SQL-script
pad_naar_sql = os.path.join("database", "schema.sql")

# Lees de SQL-instructies
with open(pad_naar_sql, "r", encoding="utf-8") as f:
    sql_script = f.read()

# Maak/verbind met database
conn = sqlite3.connect(pad_naar_db)
cursor = conn.cursor()

def new_item(item,X,Y):
    nieuw_item = (item,X,Y)
    cursor.execute("INSERT OR IGNORE INTO gebruikers")


nieuw_item = ("arduino nano", 17,15)
conn.commit()

cursor.execute("INSERT OR IGNORE INTO gebruikers (item, x,y) VALUES (?, ?,?)", nieuw_item)

conn.commit()
def lijst_items():
    pad_naar_db = os.path.join("database", "mijn_database.db")
    conn = sqlite3.connect(pad_naar_db)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM gebruikers")
    arr = []
    for rij in cursor.fetchall():
        arr.append(rij[1])
    return arr


lijst_items()

cursor.execute("SELECT * FROM gebruikers")
for rij in cursor.fetchall():
    rij[1]

conn.close()
