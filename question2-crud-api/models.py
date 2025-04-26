

from pydantic import BaseModel
from typing import Optional

class User(BaseModel):
    name: str
    email: str
    password: str

class Task(BaseModel):
    user_id: int
    title: str
    description: Optional[str] = None
    status: Optional[str] = "pending"
    due_date: Optional[str] = None

class Comment(BaseModel):
    task_id: int
    content: str
