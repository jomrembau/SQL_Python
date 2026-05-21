from mysql.connector import connect, Error
from dotenv import load_dotenv
from os import environ as env

load_dotenv()

def get_connection():

    connection = None

    try:
        connection = connect(
            host="localhost",
            port="3306",
            user="root",
            password=env.get("MYSQL_PASSWORD"),
            database="test",
            autocommit=True
        )

    except Error as e:
        print(f"Error '{e}' occurred while attempting to connect to the databank.")

    return connection

def reset():
    connection = get_connection()

    with connection.cursor() as cursor:
        with open("ddl.sql", "r") as file:
            for result in cursor.execute(file.read(), multi=True):
                pass

    connection.close()