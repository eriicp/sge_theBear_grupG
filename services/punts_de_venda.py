from sqlmodel import Session
from models.punts_de_venda import PuntDeVenda

def add_punt(Nom_Punt, Producte, Quantitat, Preu_Total, Metode_Pagament, Tiquet_Email, Data_Venda, db: Session):
    punt = PuntDeVenda(
        Nom_Punt=Nom_Punt,
        Producte=Producte,
        Quantitat=Quantitat,
        Preu_Total=Preu_Total,
        Metode_Pagament=Metode_Pagament,
        Tiquet_Email=Tiquet_Email,
        Data_Venda=Data_Venda
    )
    db.add(punt)
    db.commit()
    db.refresh(punt)
    return {"message": "Punt de venda creat correctament"}

def get_all_punts(db: Session):
    return [p.dict() for p in db.query(PuntDeVenda).all()]

def get_punt_by_id(id: int, db: Session):
    punt = db.query(PuntDeVenda).filter(PuntDeVenda.Id_Punt == id).first()
    return punt.dict() if punt else {}

def update_punt(id, Nom_Punt, Producte, Quantitat, Preu_Total, Metode_Pagament, Tiquet_Email, Data_Venda, db: Session):
    punt = db.query(PuntDeVenda).filter(PuntDeVenda.Id_Punt == id).first()
    if punt is None:
        return {}
    if Nom_Punt is not None: punt.Nom_Punt = Nom_Punt
    if Producte is not None: punt.Producte = Producte
    if Quantitat is not None: punt.Quantitat = Quantitat
    if Preu_Total is not None: punt.Preu_Total = Preu_Total
    if Metode_Pagament is not None: punt.Metode_Pagament = Metode_Pagament
    if Tiquet_Email is not None: punt.Tiquet_Email = Tiquet_Email
    if Data_Venda is not None: punt.Data_Venda = Data_Venda
    db.commit()
    db.refresh(punt)
    return punt.dict()

def delete_punt(id: int, db: Session):
    punt = db.query(PuntDeVenda).filter(PuntDeVenda.Id_Punt == id).first()
    if punt is None:
        return {}
    db.delete(punt)
    db.commit()
    return {"message": "Punt de venda eliminat correctament"}
