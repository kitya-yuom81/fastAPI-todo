from fastapi import FastAPI
from routers import todos as todos_router

app = FastAPI(title="Todo API with FastAPI", version="0.1.0")

app.include_router(todos_router.router)

@app.get("/")
def home():
    return {"message": "Welcome to FastAPI Todo Project!"}
