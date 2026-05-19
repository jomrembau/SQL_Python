import sqlite3

type(sqlite3)

conn = sqlite3.connect("first.db")

in_mem = sqlite3.connect(":memory:")

