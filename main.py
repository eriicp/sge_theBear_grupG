from fastapi import FastAPI, Depends, HTTPException, Form
from sqlmodel import SQLModel, create_engine, Session
from dotenv import load_dotenv
import os

from services import empleats, planificacio, events, costos, compres, punts_de_venda, vendes, calendari

load_dotenv()
DATABASE_URL = os.getenv("DATABASE_URL")
engine = create_engine(DATABASE_URL)
SQLModel.metadata.create_all(engine)

def get_db():
    db = Session(engine)
    try:
        yield db
    finally:
        db.close()

app = FastAPI()

# ----------- EMPLEATS ----------- 
@app.post("/empleats/", response_model=dict)
def crear_empleat(
    Nombre_Empleat: str = Form(...),
    Puesto_Empleat: str = Form(...),
    Departament_Empleat: str = Form(...),
    Email_Empleat: str = Form(...),
    Telefon_Empleat: str = Form(...),
    Id_Gerent_Empleat: int = Form(None),
    db: Session = Depends(get_db)
):
    return empleats.add_empleat(Nombre_Empleat, Puesto_Empleat, Departament_Empleat, Email_Empleat, Telefon_Empleat, Id_Gerent_Empleat, db)

@app.get("/empleats/", response_model=list[dict])
def get_empleats(db: Session = Depends(get_db)):
    return empleats.get_all_empleats(db)

@app.get("/empleats/{id}", response_model=dict)
def get_empleat(id: int, db: Session = Depends(get_db)):
    return empleats.get_empleat_by_id(id, db)

@app.put("/empleats/{id}", response_model=dict)
def update_empleat(
    id: int,
    Nombre_Empleat: str = Form(None),
    Puesto_Empleat: str = Form(None),
    Departament_Empleat: str = Form(None),
    Email_Empleat: str = Form(None),
    Telefon_Empleat: str = Form(None),
    Id_Gerent_Empleat: int = Form(None),
    db: Session = Depends(get_db)
):
    return empleats.update_empleat(id, Nombre_Empleat, Puesto_Empleat, Departament_Empleat, Email_Empleat, Telefon_Empleat, Id_Gerent_Empleat, db)

@app.delete("/empleats/{id}", response_model=dict)
def delete_empleat(id: int, db: Session = Depends(get_db)):
    return empleats.delete_empleat(id, db)



# ----------- EVENTS ----------- 
@app.post("/events/", response_model=dict)
def crear_event(
    Nom_Event: str = Form(...),
    Data_Event: str = Form(...),
    Hora_Event: str = Form(...),
    Ubicacio_Event: str = Form(...),
    Organitzador_Event: int = Form(...),
    Estat_Event: str = Form(...),
    Entrades_Disponibles: int = Form(...),
    Privat: bool = Form(...),
    db: Session = Depends(get_db)
):
    return events.add_event(Nom_Event, Data_Event, Hora_Event, Ubicacio_Event, Organitzador_Event, Estat_Event, Entrades_Disponibles, Privat, db)

@app.get("/events/", response_model=list[dict])
def get_events(db: Session = Depends(get_db)):
    return events.get_all_events(db)

@app.get("/events/{id}", response_model=dict)
def get_event(id: int, db: Session = Depends(get_db)):
    return events.get_event_by_id(id, db)

@app.put("/events/{id}", response_model=dict)
def update_event(
    id: int,
    Nom_Event: str = Form(None),
    Data_Event: str = Form(None),
    Hora_Event: str = Form(None),
    Ubicacio_Event: str = Form(None),
    Organitzador_Event: int = Form(None),
    Estat_Event: str = Form(None),
    Entrades_Disponibles: int = Form(None),
    Privat: bool = Form(None),
    db: Session = Depends(get_db)
):
    return events.update_event(id, Nom_Event, Data_Event, Hora_Event, Ubicacio_Event, Organitzador_Event, Estat_Event, Entrades_Disponibles, Privat, db)

@app.delete("/events/{id}", response_model=dict)
def delete_event(id: int, db: Session = Depends(get_db)):
    return events.delete_event(id, db)



