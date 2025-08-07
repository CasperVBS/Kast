import sqlite3

conn = sqlite3.connect("/home/pi/Desktop/Kast/oldTests/database/mijn_database.db")
cursor = conn.cursor()
cursor.execute("""
CREATE TABLE IF NOT EXISTS gebruikers (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    naam TEXT NOT NULL,
    leeftijd INTEGER
)
""")
cursor.execute("INSERT INTO gebruikers (naam, leeftijd) VALUES (?, ?)", ("Casper", 17))

conn.commit()

cursor.execute("SELECT * FROM gebruikers")
resultaten = cursor.fetchall()
for rij in resultaten:
    print(rij)

conn.close()