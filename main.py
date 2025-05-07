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





# ----------- PLANIFICACIO ----------- 
@app.post("/planificacio/", response_model=dict)
def crear_planificacio(
    Projecte: str = Form(...),
    Tasca: str = Form(...),
    Responsable: int = Form(...),
    Data_Inici: str = Form(...),
    Data_Fi: str = Form(...),
    Estat_Tasca: str = Form(...),
    Material_Utilitzat: str = Form(None),
    Comentaris: str = Form(None),
    db: Session = Depends(get_db)
):
    return planificacio.add_planificacio(Projecte, Tasca, Responsable, Data_Inici, Data_Fi, Estat_Tasca, Material_Utilitzat, Comentaris, db)

@app.get("/planificacio/", response_model=list[dict])
def get_planificacions(db: Session = Depends(get_db)):
    return planificacio.get_all_planificacions(db)

@app.get("/planificacio/{id}", response_model=dict)
def get_planificacio(id: int, db: Session = Depends(get_db)):
    return planificacio.get_planificacio_by_id(id, db)

@app.put("/planificacio/{id}", response_model=dict)
def update_planificacio(
    id: int,
    Projecte: str = Form(None),
    Tasca: str = Form(None),
    Responsable: int = Form(None),
    Data_Inici: str = Form(None),
    Data_Fi: str = Form(None),
    Estat_Tasca: str = Form(None),
    Material_Utilitzat: str = Form(None),
    Comentaris: str = Form(None),
    db: Session = Depends(get_db)
):
    return planificacio.update_planificacio(id, Projecte, Tasca, Responsable, Data_Inici, Data_Fi, Estat_Tasca, Material_Utilitzat, Comentaris, db)

#amunt valencia gora euskadi visca catalunya arriba españa 

@app.delete("/planificacio/{id}", response_model=dict)
def delete_planificacio(id: int, db: Session = Depends(get_db)):
    return planificacio.delete_planificacio(id, db)

# ----------- PUNTS DE VENDA -----------
@app.post("/punts_de_venda/", response_model=dict)
def crear_punt(
    Nom_Punt: str = Form(...),
    Producte: str = Form(...),
    Quantitat: int = Form(...),
    Preu_Total: float = Form(...),
    Metode_Pagament: str = Form(...),
    Tiquet_Email: bool = Form(...),
    Data_Venda: str = Form(...),
    db: Session = Depends(get_db)
):
    return punts_de_venda.add_punt(Nom_Punt, Producte, Quantitat, Preu_Total, Metode_Pagament, Tiquet_Email, Data_Venda, db)

@app.get("/punts_de_venda/", response_model=list[dict])
def get_punts(db: Session = Depends(get_db)):
    return punts_de_venda.get_all_punts(db)

@app.get("/punts_de_venda/{id}", response_model=dict)
def get_punt(id: int, db: Session = Depends(get_db)):
    return punts_de_venda.get_punt_by_id(id, db)

@app.put("/punts_de_venda/{id}", response_model=dict)
def update_punt(
    id: int,
    Nom_Punt: str = Form(None),
    Producte: str = Form(None),
    Quantitat: int = Form(None),
    Preu_Total: float = Form(None),
    Metode_Pagament: str = Form(None),
    Tiquet_Email: bool = Form(None),
    Data_Venda: str = Form(None),
    db: Session = Depends(get_db)
):
    return punts_de_venda.update_punt(id, Nom_Punt, Producte, Quantitat, Preu_Total, Metode_Pagament, Tiquet_Email, Data_Venda, db)

@app.delete("/punts_de_venda/{id}", response_model=dict)
def delete_punt(id: int, db: Session = Depends(get_db)):
    return punts_de_venda.delete_punt(id, db)

# ----------- VENDES -----------
@app.post("/vendes/", response_model=dict)
def crear_venda(
    Data_Venda: str = Form(...),
    Client_Venda: str = Form(...),
    Producte_Venda: str = Form(...),
    Quantitat: int = Form(...),
    Preu_Unitari: float = Form(...),
    Total: float = Form(...),
    Metode_Pagament: str = Form(...),
    Id_Punt: int = Form(...),
    db: Session = Depends(get_db)
):
    return vendes.add_venda(Data_Venda, Client_Venda, Producte_Venda, Quantitat, Preu_Unitari, Total, Metode_Pagament, Id_Punt, db)

@app.get("/vendes/", response_model=list[dict])
def get_vendes(db: Session = Depends(get_db)):
    return vendes.get_all_vendes(db)

@app.get("/vendes/{id}", response_model=dict)
def get_venda(id: int, db: Session = Depends(get_db)):
    return vendes.get_venda_by_id(id, db)

@app.put("/vendes/{id}", response_model=dict)
def update_venda(
    id: int,
    Data_Venda: str = Form(None),
    Client_Venda: str = Form(None),
    Producte_Venda: str = Form(None),
    Quantitat: int = Form(None),
    Preu_Unitari: float = Form(None),
    Total: float = Form(None),
    Metode_Pagament: str = Form(None),
    Id_Punt: int = Form(None),
    db: Session = Depends(get_db)
):
    return vendes.update_venda(id, Data_Venda, Client_Venda, Producte_Venda, Quantitat, Preu_Unitari, Total, Metode_Pagament, Id_Punt, db)

@app.delete("/vendes/{id}", response_model=dict)
def delete_venda(id: int, db: Session = Depends(get_db)):
    return vendes.delete_venda(id, db)

# ----------- CALENDARI -----------
@app.post("/calendari/", response_model=dict)
def crear_reunio(
    Nom_Reunio: str = Form(...),
    Data_Reunio: str = Form(...),
    Hora_Inici: str = Form(...),
    Hora_Fi: str = Form(...),
    Ubicacio_Reunio: str = Form(...),
    Etiquetes: str = Form(None),
    Recurrencia: bool = Form(False),
    db: Session = Depends(get_db)
):
    return calendari.add_reunio(Nom_Reunio, Data_Reunio, Hora_Inici, Hora_Fi, Ubicacio_Reunio, Etiquetes, Recurrencia, db)

@app.get("/calendari/", response_model=list[dict])
def get_reunions(db: Session = Depends(get_db)):
    return calendari.get_all_reunions(db)

@app.get("/calendari/{id}", response_model=dict)
def get_reunio(id: int, db: Session = Depends(get_db)):
    return calendari.get_reunio_by_id(id, db)

@app.put("/calendari/{id}", response_model=dict)
def update_reunio(
    id: int,
    Nom_Reunio: str = Form(None),
    Data_Reunio: str = Form(None),
    Hora_Inici: str = Form(None),
    Hora_Fi: str = Form(None),
    Ubicacio_Reunio: str = Form(None),
    Etiquetes: str = Form(None),
    Recurrencia: bool = Form(None),
    db: Session = Depends(get_db)
):
    return calendari.update_reunio(id, Nom_Reunio, Data_Reunio, Hora_Inici, Hora_Fi, Ubicacio_Reunio, Etiquetes, Recurrencia, db)

@app.delete("/calendari/{id}", response_model=dict)
def delete_reunio(id: int, db: Session = Depends(get_db)):
    return calendari.delete_reunio(id, db)


