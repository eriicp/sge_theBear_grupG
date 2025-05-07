from sqlmodel import Session
from models.empleats import Empleat

def add_empleat(Nombre_Empleat, Puesto_Empleat, Departament_Empleat, Email_Empleat, Telefon_Empleat, Id_Gerent_Empleat, db: Session):
    empleat = Empleat(
        Nombre_Empleat=Nombre_Empleat,
        Puesto_Empleat=Puesto_Empleat,
        Departament_Empleat=Departament_Empleat,
        Email_Empleat=Email_Empleat,
        Telefon_Empleat=Telefon_Empleat,
        Id_Gerent_Empleat=Id_Gerent_Empleat
    )
    db.add(empleat)
    db.commit()
    db.refresh(empleat)
    return {"message": "Empleat creat correctament"}

def get_all_empleats(db: Session):
    return [e.dict() for e in db.query(Empleat).all()]

def get_empleat_by_id(id: int, db: Session):
    return db.query(Empleat).filter(Empleat.Id_Empleat == id).first().dict()

def update_empleat(id, Nombre_Empleat, Puesto_Empleat, Departament_Empleat, Email_Empleat, Telefon_Empleat, Id_Gerent_Empleat, db: Session):
    empleat = db.query(Empleat).filter(Empleat.Id_Empleat == id).first()
    if Nombre_Empleat is not None: empleat.Nombre_Empleat = Nombre_Empleat
    if Puesto_Empleat is not None: empleat.Puesto_Empleat = Puesto_Empleat
    if Departament_Empleat is not None: empleat.Departament_Empleat = Departament_Empleat
    if Email_Empleat is not None: empleat.Email_Empleat = Email_Empleat
    if Telefon_Empleat is not None: empleat.Telefon_Empleat = Telefon_Empleat
    if Id_Gerent_Empleat is not None: empleat.Id_Gerent_Empleat = Id_Gerent_Empleat
    db.commit()
    db.refresh(empleat)
    return empleat.dict()

def delete_empleat(id: int, db: Session):
    empleat = db.query(Empleat).filter(Empleat.Id_Empleat == id).first()
    db.delete(empleat)
    db.commit()
    return {"message": "Empleat eliminat correctament"}
