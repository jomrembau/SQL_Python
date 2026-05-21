import typer
from rich.console import Console
from mysql.connector import connect
from dotenv import load_dotenv
import os

load_dotenv()

connection = connect(
    host="localhost",
    port="3306",
    user="root",
    password=os.getenv("MYSQL_PASSWORD"),
    database="test",
    autocommit=True
)

app = typer = typer.Typer()
console = Console()

@app.command()
def add_student():
    console.print("Adding a new student..")

if __name__ == "__main__":
    app()
