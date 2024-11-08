from fastapi import FastAPI

app = FastAPI()

@app.get("/ping")
def read_ping():
    return {"message": "pong"}

@app.get("/")
def read_root():
    return "Hello, World!"
