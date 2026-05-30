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



    def get(self, table: str, columns: list[str], limit: int = None, where: dict = None):
        query = sql.SQL("SELECT {} FROM {}").format(
            sql.SQL(',').join(map(sql.Identifier, columns)),
            sql.Identifier(table)
        )

        if where:
            query += sql.SQL(" WHERE {}").format(
                sql.SQL(" AND ").join(
                    map(
                        lambda x: sql.SQL("{} = {}").format(
                            sql.Identifier(x),
                            sql.Literal(where.get(x))
                        ), where)
                )
            )

        if limit:
            query += sql.SQL("LIMIT {}").format(sql.Literal(limit))

        self.cursor.execute(query)
        return self.cursor.fetchall()

    def get_one(self, table: str, columns: list[str], where: dict = None):
        result =  self.get(table, columns, 1, where)

        if len(result):
            return result[0]
