from fastapi import APIRouter

router = APIRouter()

@router.get("/punts_de_venda")
def read_punts_de_venda():
    return {"message": "List of points of sale"}

@router.post("/punts_de_venda")
def create_punt_de_venda(punt_de_venda: dict):
    return {"message": "Point of sale created", "data": punt_de_venda}

@router.get("/punts_de_venda/{punt_id}")
def read_punt_de_venda(punt_id: int):
    return {"message": "Details of point of sale", "id": punt_id}

@router.put("/punts_de_venda/{punt_id}")
def update_punt_de_venda(punt_id: int, punt_de_venda: dict):
    return {"message": "Point of sale updated", "id": punt_id, "data": punt_de_venda}

@router.delete("/punts_de_venda/{punt_id}")
def delete_punt_de_venda(punt_id: int):
    return {"message": "Point of sale deleted", "id": punt_id}