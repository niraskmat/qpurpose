from pydantic import BaseModel, ConfigDict
from typing import Optional
from datetime import datetime

class UserCreate(BaseModel):
    username: str
    password: str

class UserOut(BaseModel):
    model_config = ConfigDict(from_attributes=True, extra='ignore')
    id: int
    username: str

class Token(BaseModel):
    access_token: str
    token_type: str

class TaskBase(BaseModel):
    model_config = ConfigDict(from_attributes=True, extra='ignore')
    title: Optional[str] = None
    description: Optional[str] = None
    start_date: Optional[datetime] = None
    due_date: Optional[datetime] = None
    completed: Optional[bool] = None

class TaskCreate(TaskBase):
    title: str

class TaskOut(TaskBase):
    model_config = ConfigDict(from_attributes=True, extra='ignore')
    id: int
    owner_id: int

class TaskUpdate(TaskBase):
    pass
