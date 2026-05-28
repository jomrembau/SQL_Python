from fastapi import FastAPI, Depends
from database import Database
from pydantic import BaseModel, EmailStr

class User(BaseModel):
    email: str
    password: str

class ValidatedUser(BaseModel):
    email: EmailStr
    password: str

User(email="a@gmail.com", password= "b")

app = FastAPI()

def get_db():
    db = Database()

    try:
        db.open()
        yield db

    finally:
        db.close()

@app.get("/")
def root():
    return {"message" : "empty message. hello"}

@app.get("/hello")
def hello(db: Database = Depends(get_db)):
    return {"message" : "Hello, World"}

@app.get("/register")
def register(email: str, password: str):
    return {"email": email, "password": password}