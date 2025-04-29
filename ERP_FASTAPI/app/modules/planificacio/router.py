from fastapi import APIRouter

router = APIRouter()

@router.get("/planning")
def get_planning():
    return {"message": "List of planning items"}

@router.post("/planning")
def create_planning(item: dict):
    return {"message": "Planning item created", "item": item}

@router.put("/planning/{item_id}")
def update_planning(item_id: int, item: dict):
    return {"message": "Planning item updated", "item_id": item_id, "item": item}

@router.delete("/planning/{item_id}")
def delete_planning(item_id: int):
    return {"message": "Planning item deleted", "item_id": item_id}