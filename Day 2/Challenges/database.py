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

def add_a_student(first_name,last_name,unix_id):
    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute("INSERT INTO students(first_name,last_name,unix_id) VALUES (%s, %s, %s);",
                        (first_name,last_name,unix_id))
            conn.commit()

def add_a_course(moniker,name,department):
    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute("INSERT INTO courses(moniker,name,department) VALUES (%s, %s, %s);",
                        (moniker,name,department))
            conn.commit()

def add_a_prerequisite(course, prereq,min_grade):
    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute("INSERT INTO prerequisites(course,prereq,min_grade) VALUES (%s, %s, %s);",
                        (course,prereq,min_grade))
            conn.commit()
