from sqlmodel import Session
from models.compres import Compra

def add_compra(Data_Compra, Proveidor, Producte_Compra, Quantitat, Preu_Unitari, Total, Estat_Comanda, db: Session):
    compra = Compra(
        Data_Compra=Data_Compra,
        Proveidor=Proveidor,
        Producte_Compra=Producte_Compra,
        Quantitat=Quantitat,
        Preu_Unitari=Preu_Unitari,
        Total=Total,
        Estat_Comanda=Estat_Comanda
    )
    db.add(compra)
    db.commit()
    db.refresh(compra)
    return {"message": "Compra creada correctament"}

def get_all_compres(db: Session):
    return [c.dict() for c in db.query(Compra).all()]

def get_compra_by_id(id: int, db: Session):
    compra = db.query(Compra).filter(Compra.Id_Compra == id).first()
    return compra.dict() if compra else {}

def update_compra(id, Data_Compra, Proveidor, Producte_Compra, Quantitat, Preu_Unitari, Total, Estat_Comanda, db: Session):
    compra = db.query(Compra).filter(Compra.Id_Compra == id).first()
    if compra is None:
        return {}
    if Data_Compra is not None: compra.Data_Compra = Data_Compra
    if Proveidor is not None: compra.Proveidor = Proveidor
    if Producte_Compra is not None: compra.Producte_Compra = Producte_Compra
    if Quantitat is not None: compra.Quantitat = Quantitat
    if Preu_Unitari is not None: compra.Preu_Unitari = Preu_Unitari
    if Total is not None: compra.Total = Total
    if Estat_Comanda is not None: compra.Estat_Comanda = Estat_Comanda
    db.commit()
    db.refresh(compra)
    return compra.dict()

def delete_compra(id: int, db: Session):
    compra = db.query(Compra).filter(Compra.Id_Compra == id).first()
    if compra is None:
        return {}
    db.delete(compra)
    db.commit()
    return {"message": "Compra eliminada correctament"}
