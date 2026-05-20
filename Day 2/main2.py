from mysql.connector import connect
from dotenv import load_dotenv
import os

load_dotenv()

get_db_connection = lambda: connect(
    host="localhost",
    port="3306",
    user="root",
    password=os.getenv("MYSQL_PASSWORD"),
    database="test",
    autocommit=True
)

query = "INSERT INTO users (username,password) VALUES (%s,%s);"

users = [
    ("bob"," 786"),
    ("aris", "thg"),
    ("annie", "jjhg")
]

# with get_db_connection() as conn:
#    with conn.cursor() as cur:

#        cur.execute("""
#            INSERT INTO users(username,password)
#            Values
#            ("Ben", "1234"),
#            ("Yan", "5678")
#        """)


with get_db_connection() as conn:
    with conn.cursor() as cur:
        cur.executemany(query,users)

