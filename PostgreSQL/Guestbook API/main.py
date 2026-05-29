from fastapi import FastAPI, Depends, Query
from database import Database
from pydantic import BaseModel, EmailStr, ValidationError, SecretStr
from utils import get_password_hash, verify_password

app = FastAPI()


class User(BaseModel):
    email: EmailStr
    password: SecretStr


def get_db():
    db = Database()

    try:
        db.open()
        yield db
    finally:
        db.close()


@app.get("/")
def root():
    return {"message": "empty message. hello"}


@app.get("/hello")
def hello(db: Database = Depends(get_db)):
    return {"message": "Hello, World"}


@app.post("/register")
def register(email: str, password: SecretStr = Query(default=None, min_length=8), db: Database = Depends(get_db)):
    try:

        user = User(email=email, password=password)
        hashed_password = get_password_hash(password.get_secret_value())

        with db.conn:
            db.cursor.execute("INSERT INTO users (email,password) VALUES (%s,%s)",(user.email, hashed_password))

        return {
            "message": "User successfully created."
        }

    except ValidationError:
        return {
            "Error": "Not a valid email"
        }