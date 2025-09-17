# models.py
from typing import Optional
from pydantic import BaseModel, Field

# schema for creating a todo
class TodoIn(BaseModel):
    title: str = Field(min_length=1, max_length=200)
    completed: bool = False

# schema for partial update
class TodoUpdate(BaseModel):
    title: Optional[str] = Field(default=None, min_length=1, max_length=200)
    completed: Optional[bool] = None

# schema for responses (includes id)
class TodoOut(TodoIn):
    id: int
