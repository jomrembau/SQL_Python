from fastapi import FastAPI
from database import Database

app = FastAPI()
db = Database()

@app.get("/")
def root():
    return {"message" : "empty message"}

@app.get("/hello")
def hello():
    return "Hello, World^!"