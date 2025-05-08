from sqlmodel import Session
from models.vendes import Venda

def add_venda(Data_Venda, Client_Venda, Producte_Venda, Quantitat, Preu_Unitari, Total, Metode_Pagament, Id_Punt, db: Session):
    venda = Venda(
        Data_Venda=Data_Venda,
        Client_Venda=Client_Venda,
        Producte_Venda=Producte_Venda,
        Quantitat=Quantitat,
        Preu_Unitari=Preu_Unitari,
        Total=Total,
        Metode_Pagament=Metode_Pagament,
        Id_Punt=Id_Punt
    )
    db.add(venda)
    db.commit()
    db.refresh(venda)
    return {"message": "Venda creada correctament"}

def get_all_vendes(db: Session):
    return [v.dict() for v in db.query(Venda).all()]

def get_venda_by_id(id: int, db: Session):
    venda = db.query(Venda).filter(Venda.Id_Venda == id).first()
    return venda.dict() if venda else {}

def update_venda(id, Data_Venda, Client_Venda, Producte_Venda, Quantitat, Preu_Unitari, Total, Metode_Pagament, Id_Punt, db: Session):
    venda = db.query(Venda).filter(Venda.Id_Venda == id).first()
    if venda is None:
        return {}
    if Data_Venda is not None: venda.Data_Venda = Data_Venda
    if Client_Venda is not None: venda.Client_Venda = Client_Venda
    if Producte_Venda is not None: venda.Producte_Venda = Producte_Venda
    if Quantitat is not None: venda.Quantitat = Quantitat
    if Preu_Unitari is not None: venda.Preu_Unitari = Preu_Unitari
    if Total is not None: venda.Total = Total
    if Metode_Pagament is not None: venda.Metode_Pagament = Metode_Pagament
    if Id_Punt is not None: venda.Id_Punt = Id_Punt
    db.commit()
    db.refresh(venda)
    return venda.dict()

def delete_venda(id: int, db: Session):
    venda = db.query(Venda).filter(Venda.Id_Venda == id).first()
    if venda is None:
        return {}
    db.delete(venda)
    db.commit()
    return {"message": "Venda eliminada correctament"}
