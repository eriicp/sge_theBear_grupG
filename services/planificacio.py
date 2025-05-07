from sqlmodel import Session
from models.planificacio import Planificacio

def add_planificacio(Projecte, Tasca, Responsable, Data_Inici, Data_Fi, Estat_Tasca, Material_Utilitzat, Comentaris, db: Session):
    plan = Planificacio(
        Projecte=Projecte,
        Tasca=Tasca,
        Responsable=Responsable,
        Data_Inici=Data_Inici,
        Data_Fi=Data_Fi,
        Estat_Tasca=Estat_Tasca,
        Material_Utilitzat=Material_Utilitzat,
        Comentaris=Comentaris
    )
    db.add(plan)
    db.commit()
    db.refresh(plan)
    return {"message": "Planificació creada correctament"}

def get_all_planificacions(db: Session):
    return [p.dict() for p in db.query(Planificacio).all()]

def get_planificacio_by_id(id: int, db: Session):
    plan = db.query(Planificacio).filter(Planificacio.Id_Planificacio == id).first()
    return plan.dict() if plan else {}

def update_planificacio(id, Projecte, Tasca, Responsable, Data_Inici, Data_Fi, Estat_Tasca, Material_Utilitzat, Comentaris, db: Session):
    plan = db.query(Planificacio).filter(Planificacio.Id_Planificacio == id).first()
    if plan is None:
        return {}
    if Projecte is not None: plan.Projecte = Projecte
    if Tasca is not None: plan.Tasca = Tasca
    if Responsable is not None: plan.Responsable = Responsable
    if Data_Inici is not None: plan.Data_Inici = Data_Inici
    if Data_Fi is not None: plan.Data_Fi = Data_Fi
    if Estat_Tasca is not None: plan.Estat_Tasca = Estat_Tasca
    if Material_Utilitzat is not None: plan.Material_Utilitzat = Material_Utilitzat
    if Comentaris is not None: plan.Comentaris = Comentaris
    db.commit()
    db.refresh(plan)
    return plan.dict()

def delete_planificacio(id: int, db: Session):
    plan = db.query(Planificacio).filter(Planificacio.Id_Planificacio == id).first()
    if plan is None:
        return {}
    db.delete(plan)
    db.commit()
    return {"message": "Planificació eliminada correctament"}
