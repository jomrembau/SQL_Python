from mysql.connector import connect
from dotenv import load_dotenv
import os

load_dotenv()

connection = connect(
    host="localhost",
    port="3306",
    user="root",
    password=os.getenv("MYSQL_PASSWORD"),
    database="test"
)

print(connection.is_connected())

cur = connection.cursor()

cur.execute("DROP TABLE IF EXISTS users;")

cur.execute("""
    CREATE TABLE users (
      id INTEGER PRIMARY KEY AUTO_INCREMENT,
      username VARCHAR(50) NOT NULL,
      password VARCHAR(50) NOT NULL
    );
""")

cur.execute("""
    INSERT INTO users(username,password) 
    Values
    ("James", "1234"),
    ("Ryan", "5678")
""")

connection.commit()

connection.close()

