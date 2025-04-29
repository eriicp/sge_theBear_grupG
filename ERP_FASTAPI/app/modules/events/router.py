from fastapi import APIRouter

router = APIRouter()

@router.get("/events")
def read_events():
    return {"message": "List of events"}

@router.post("/events")
def create_event(event: dict):
    return {"message": "Event created", "event": event}

@router.get("/events/{event_id}")
def read_event(event_id: int):
    return {"message": "Event details", "event_id": event_id}

@router.put("/events/{event_id}")
def update_event(event_id: int, event: dict):
    return {"message": "Event updated", "event_id": event_id, "event": event}

@router.delete("/events/{event_id}")
def delete_event(event_id: int):
    return {"message": "Event deleted", "event_id": event_id}