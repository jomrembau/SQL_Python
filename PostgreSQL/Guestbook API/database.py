from psycopg2 import connect, sql
from psycopg2.extras import RealDictCursor
import os
from dotenv import load_dotenv

load_dotenv()

class Database:

    def __init__(self):
        self.conn = None
        self.cursor = None

    def open(self):
        self.conn = connect(
            host="localhost",
            port=5433,
            user="postgres",
            password=os.getenv("postgresql_pw"),
            database="guestbook"
        )
        self.cursor = self.conn.cursor(cursor_factory=RealDictCursor)

    def close(self):
        self.cursor.close()
        self.conn.close()

    def write(self, table: str, columns: list, data: list[str]):
        query = sql.SQL("INSERT INTO {} ({}) VALUES ({}) RETURNING id").format(
            sql.Identifier(table),
            sql.SQL(",").join(map(sql.Identifier, columns)),
            sql.SQL(",").join(map(sql.Literal, data)),
        )

        self.cursor.execute(query)
        self.conn.commit()
        return self.cursor.fetchone().get("id")
