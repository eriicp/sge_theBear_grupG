from fastapi import APIRouter

router = APIRouter()

@router.get("/costos")
def read_costos():
    return {"message": "List of costs"}

@router.post("/costos")
def create_costo(costo: dict):
    return {"message": "Cost created", "costo": costo}

@router.get("/costos/{costo_id}")
def read_costo(costo_id: int):
    return {"message": "Cost details", "costo_id": costo_id}

@router.put("/costos/{costo_id}")
def update_costo(costo_id: int, costo: dict):
    return {"message": "Cost updated", "costo_id": costo_id, "costo": costo}

@router.delete("/costos/{costo_id}")
def delete_costo(costo_id: int):
    return {"message": "Cost deleted", "costo_id": costo_id}