from typing import Optional
from pydantic import BaseModel, Field

class TodoIn(BaseModel):
    title: str = Field(min_length=1, max_length=200)
    completed: bool = False

class TodoUpdate(BaseModel):
    title: Optional[str] = Field(default=None, min_length=1, max_length=200)
    completed: Optional[bool] = None

class TodoOut(TodoIn):
    id: int
