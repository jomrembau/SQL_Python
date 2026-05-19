import sqlite3

type(sqlite3)

conn = sqlite3.connect("first.db")

cur = conn.cursor()

cur.execute("""
    CREATE TABLE ice_cream_flavors (
        id INTEGER PRIMARY KEY,
        flavor TEXT,
        rating INTEGER
        ); 
        """)




