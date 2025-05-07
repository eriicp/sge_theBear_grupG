from sqlmodel import Session
from models.calendari import Reunio

def add_reunio(Nom_Reunio, Data_Reunio, Hora_Inici, Hora_Fi, Ubicacio_Reunio, Etiquetes, Recurrencia, db: Session):
    reunio = Reunio(
        Nom_Reunio=Nom_Reunio,
        Data_Reunio=Data_Reunio,
        Hora_Inici=Hora_Inici,
        Hora_Fi=Hora_Fi,
        Ubicacio_Reunio=Ubicacio_Reunio,
        Etiquetes=Etiquetes,
        Recurrencia=Recurrencia
    )
    db.add(reunio)
    db.commit()
    db.refresh(reunio)
    return {"message": "Reunió creada correctament"}

def get_all_reunions(db: Session):
    return [r.dict() for r in db.query(Reunio).all()]

def get_reunio_by_id(id: int, db: Session):
    reunio = db.query(Reunio).filter(Reunio.Id_Reunio == id).first()
    return reunio.dict() if reunio else {}

def update_reunio(id, Nom_Reunio, Data_Reunio, Hora_Inici, Hora_Fi, Ubicacio_Reunio, Etiquetes, Recurrencia, db: Session):
    reunio = db.query(Reunio).filter(Reunio.Id_Reunio == id).first()
    if reunio is None:
        return {}
    if Nom_Reunio is not None: reunio.Nom_Reunio = Nom_Reunio
    if Data_Reunio is not None: reunio.Data_Reunio = Data_Reunio
    if Hora_Inici is not None: reunio.Hora_Inici = Hora_Inici
    if Hora_Fi is not None: reunio.Hora_Fi = Hora_Fi
    if Ubicacio_Reunio is not None: reunio.Ubicacio_Reunio = Ubicacio_Reunio
    if Etiquetes is not None: reunio.Etiquetes = Etiquetes
    if Recurrencia is not None: reunio.Recurrencia = Recurrencia
    db.commit()
    db.refresh(reunio)
    return reunio.dict()

def delete_reunio(id: int, db: Session):
    reunio = db.query(Reunio).filter(Reunio.Id_Reunio == id).first()
    if reunio is None:
        return {}
    db.delete(reunio)
    db.commit()
    return {"message": "Reunió eliminada correctament"}
