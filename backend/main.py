from fastapi import FastAPI
import uvicorn

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Welcome to FastAPI E-commerce Backend!"}
