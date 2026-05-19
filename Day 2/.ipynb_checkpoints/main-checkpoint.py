from mysql.connector import connect
import os

connection = connect(
    host="localhost",
    port="3306",
    user="root",
    password=os.getenv("MYSQL_PASSWORD"),
    database="test"
)

print(connection.is_connected())

connection.close()

test