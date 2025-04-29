from pydantic import BaseModel
from datetime import datetime

class CalendarEvent(BaseModel):
    id: int
    title: str
    description: str
    start_time: datetime
    end_time: datetime
    location: str

class Calendar(BaseModel):
    id: int
    name: str
    events: list[CalendarEvent] = []