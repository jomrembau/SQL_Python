import typer
from rich.console import Console

app = typer = typer.Typer()
console = Console()

@app.command()
def add_student():
    console.print("Adding a new student..")

if __name__ == "__main__":
    app()
