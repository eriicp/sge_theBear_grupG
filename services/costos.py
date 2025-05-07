from sqlmodel import Session
from models.costos import Cost

def add_cost(Descripcio, Categoria, Quantitat, Data_Cost, Pagat_Per, db: Session):
    cost = Cost(
        Descripcio=Descripcio,
        Categoria=Categoria,
        Quantitat=Quantitat,
        Data_Cost=Data_Cost,
        Pagat_Per=Pagat_Per
    )
    db.add(cost)
    db.commit()
    db.refresh(cost)
    return {"message": "Cost creat correctament"}

def get_all_costos(db: Session):
    return [c.dict() for c in db.query(Cost).all()]

def get_cost_by_id(id: int, db: Session):
    cost = db.query(Cost).filter(Cost.Id_Cost == id).first()
    return cost.dict() if cost else {}

def update_cost(id, Descripcio, Categoria, Quantitat, Data_Cost, Pagat_Per, db: Session):
    cost = db.query(Cost).filter(Cost.Id_Cost == id).first()
    if cost is None:
        return {}
    if Descripcio is not None: cost.Descripcio = Descripcio
    if Categoria is not None: cost.Categoria = Categoria
    if Quantitat is not None: cost.Quantitat = Quantitat
    if Data_Cost is not None: cost.Data_Cost = Data_Cost
    if Pagat_Per is not None: cost.Pagat_Per = Pagat_Per
    db.commit()
    db.refresh(cost)
    return cost.dict()

def delete_cost(id: int, db: Session):
    cost = db.query(Cost).filter(Cost.Id_Cost == id).first()
    if cost is None:
        return {}
    db.delete(cost)
    db.commit()
    return {"message": "Cost eliminat correctament"}
