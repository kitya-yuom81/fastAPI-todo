# routers/todos.py
from fastapi import APIRouter, HTTPException
from models import TodoIn, TodoUpdate, TodoOut
from database import todos

router = APIRouter(prefix="/todos", tags=["todos"])

def _find_index(todo_id: int) -> int:
    for i, t in enumerate(todos):
        if t["id"] == todo_id:
            return i
    return -1

@router.get("/", response_model=list[TodoOut])
def list_todos():
    return todos

@router.get("/{todo_id}", response_model=TodoOut)
def get_todo(todo_id: int):
    i = _find_index(todo_id)
    if i == -1:
        raise HTTPException(status_code=404, detail="Todo not found")
    return todos[i]

@router.post("/", response_model=TodoOut, status_code=201)
def create_todo(data: TodoIn):
    new_id = (todos[-1]["id"] + 1) if todos else 1
    item = {"id": new_id, **data.model_dump()}
    todos.append(item)
    return item

@router.put("/{todo_id}", response_model=TodoOut)
def replace_todo(todo_id: int, data: TodoIn):
    i = _find_index(todo_id)
    if i == -1:
        raise HTTPException(status_code=404, detail="Todo not found")
    todos[i] = {"id": todo_id, **data.model_dump()}
    return todos[i]

@router.patch("/{todo_id}", response_model=TodoOut)
def patch_todo(todo_id: int, data: TodoUpdate):
    i = _find_index(todo_id)
    if i == -1:
        raise HTTPException(status_code=404, detail="Todo not found")
    changed = data.model_dump(exclude_unset=True)
    todos[i].update(changed)
    return todos[i]

@router.delete("/{todo_id}", status_code=204)
def delete_todo(todo_id: int):
    i = _find_index(todo_id)
    if i == -1:
        raise HTTPException(status_code=404, detail="Todo not found")
    todos.pop(i)
