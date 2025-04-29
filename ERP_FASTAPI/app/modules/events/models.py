from pydantic import BaseModel
from datetime import datetime

class Event(BaseModel):
    id: int
    name: str
    description: str
    start_time: datetime
    end_time: datetime
    location: str

class EventCreate(BaseModel):
    name: str
    description: str
    start_time: datetime
    end_time: datetime
    location: str

class EventUpdate(BaseModel):
    name: str = None
    description: str = None
    start_time: datetime = None
    end_time: datetime = None
    location: str = None