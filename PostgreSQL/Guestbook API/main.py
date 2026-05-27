from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"message" : "empty message"}

@app.get("/hello")
def hello():
    return "Hello, World^!"