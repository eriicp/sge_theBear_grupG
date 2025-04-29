from fastapi import APIRouter

router = APIRouter()

@router.get("/calendars")
def get_calendars():
    return {"message": "List of calendars"}

@router.post("/calendars")
def create_calendar(calendar: dict):
    return {"message": "Calendar created", "calendar": calendar}

@router.get("/calendars/{calendar_id}")
def get_calendar(calendar_id: int):
    return {"message": f"Details of calendar {calendar_id}"}

@router.put("/calendars/{calendar_id}")
def update_calendar(calendar_id: int, calendar: dict):
    return {"message": f"Calendar {calendar_id} updated", "calendar": calendar}

@router.delete("/calendars/{calendar_id}")
def delete_calendar(calendar_id: int):
    return {"message": f"Calendar {calendar_id} deleted"}