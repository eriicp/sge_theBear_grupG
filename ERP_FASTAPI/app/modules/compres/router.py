from fastapi import APIRouter

router = APIRouter()

@router.get("/compres")
def read_compres():
    return {"message": "List of purchases"}

@router.post("/compres")
def create_compra(compra: dict):
    return {"message": "Purchase created", "compra": compra}

@router.get("/compres/{compra_id}")
def read_compra(compra_id: int):
    return {"message": "Details of purchase", "compra_id": compra_id}

@router.put("/compres/{compra_id}")
def update_compra(compra_id: int, compra: dict):
    return {"message": "Purchase updated", "compra_id": compra_id, "compra": compra}

@router.delete("/compres/{compra_id}")
def delete_compra(compra_id: int):
    return {"message": "Purchase deleted", "compra_id": compra_id}