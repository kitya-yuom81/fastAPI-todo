from fastapi import APIRouter, HTTPException
from models import Todo
from database import todos


router = APIRouter(prefix="/todos", tags=["todos"])

# Get all todos
@router.get("/")
def get_todos():
    return todos

# Get a single todo
@router.get("/{todo_id}")
def get_todo(todo_id: int):
    for todo in todos:
        if todo["id"] == todo_id:
            return todo
    raise HTTPException(status_code=404, detail="Todo not found")

# Create a new todo
@router.post("/")
def create_todo(todo: Todo):
    todo.id = len(todos) + 1
    todos.append(todo.dict())  # fixed typo
    return todo
@router.delete("/{todo_id}")
def delete_todo(todo_id: int):
    for idx, todo in enumerate(todos):
        if todo["id"] == todo_id:
            deleted = todos.pop(idx)
            return {"message": "Todo deleted", "todo": deleted}
    raise HTTPException(status_code=404, detail="Todo not found")