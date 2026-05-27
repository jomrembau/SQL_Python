from fastapi import FastAPI, Depends
from database import Database

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