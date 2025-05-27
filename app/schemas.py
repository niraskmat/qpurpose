from pydantic import BaseModel, ConfigDict, model_validator
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

    @model_validator(mode="before")
    @classmethod
    def parse_dates(cls, data):
        if not isinstance(data, dict):
            return data

        for field in ("start_date", "due_date"):
            if field not in data.keys():
                continue
            raw_value = data[field]
            if isinstance(raw_value, datetime) or raw_value is None:
                continue
            for fmt in ("%Y-%m-%d", "%Y/%m/%d", "%d-%m-%Y", "%d/%m/%Y"):
                try:

                    data[field] = datetime.strptime(raw_value, fmt)
                    break
                except (ValueError, TypeError):
                    continue
            else:
                raise ValueError(
                    f"Invalid date format for '{field}'. Use YYYY-MM-DD, YYYY/MM/DD, DD-MM-YYYY, or DD/MM/YYYY."
                )
        return data

    @model_validator(mode="after")
    def validate_date_order(self):
        if self.start_date and self.due_date:
            if self.start_date > self.due_date:
                raise ValueError("start_date must not be after due_date.")
        return self

class TaskCreate(TaskBase):
    title: str

class TaskOut(TaskBase):
    model_config = ConfigDict(from_attributes=True, extra='ignore')
    id: int
    owner_id: int

class TaskUpdate(TaskBase):
    pass
