from fastapi import FastAPI
from routers import todos

app = FastAPI(title="Todo API with FastAPI")

app.include_router(todos.router)

@app.get("/")
def home():
    return {"message": "Welcome to FastAPI Todo Project!"}
