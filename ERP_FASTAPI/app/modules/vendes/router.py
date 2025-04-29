from fastapi import APIRouter

router = APIRouter()

@router.get("/vendes")
def read_vendes():
    return {"message": "List of sales"}

@router.post("/vendes")
def create_venda(venda: dict):
    return {"message": "Venda created", "venda": venda}

@router.get("/vendes/{venda_id}")
def read_venda(venda_id: int):
    return {"message": "Details of venda", "venda_id": venda_id}

@router.put("/vendes/{venda_id}")
def update_venda(venda_id: int, venda: dict):
    return {"message": "Venda updated", "venda_id": venda_id, "venda": venda}

@router.delete("/vendes/{venda_id}")
def delete_venda(venda_id: int):
    return {"message": "Venda deleted", "venda_id": venda_id}