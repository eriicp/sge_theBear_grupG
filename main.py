from fastapi import FastAPI, Depends, Form
from sqlmodel import SQLModel, create_engine, Session
from dotenv import load_dotenv
import os

from services import  costos, compres

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
# ----------- COSTOS ----------- 
@app.post("/costos/", response_model=dict)
def crear_cost(
    Descripcio: str = Form(...),
    Categoria: str = Form(...),
    Quantitat: float = Form(...),
    Data_Cost: str = Form(...),
    Pagat_Per: int = Form(...),
    db: Session = Depends(get_db)
):
    return costos.add_cost(Descripcio, Categoria, Quantitat, Data_Cost, Pagat_Per, db)

@app.get("/costos/", response_model=list[dict])
def get_costos(db: Session = Depends(get_db)):
    return costos.get_all_costos(db)

@app.get("/costos/{id}", response_model=dict)
def get_cost(id: int, db: Session = Depends(get_db)):
    return costos.get_cost_by_id(id, db)

@app.put("/costos/{id}", response_model=dict)
def update_cost(
    id: int,
    Descripcio: str = Form(None),
    Categoria: str = Form(None),
    Quantitat: float = Form(None),
    Data_Cost: str = Form(None),
    Pagat_Per: int = Form(None),
    db: Session = Depends(get_db)
):
    return costos.update_cost(id, Descripcio, Categoria, Quantitat, Data_Cost, Pagat_Per, db)

@app.delete("/costos/{id}", response_model=dict)
def delete_cost(id: int, db: Session = Depends(get_db)):
    return costos.delete_cost(id, db)

# ----------- COMPRES -----------
@app.post("/compres/", response_model=dict)
def crear_compra(
    Data_Compra: str = Form(...),
    Proveidor: str = Form(...),
    Producte_Compra: str = Form(...),
    Quantitat: int = Form(...),
    Preu_Unitari: float = Form(...),
    Total: float = Form(...),
    Estat_Comanda: str = Form(...),
    db: Session = Depends(get_db)
):
    return compres.add_compra(Data_Compra, Proveidor, Producte_Compra, Quantitat, Preu_Unitari, Total, Estat_Comanda, db)

@app.get("/compres/", response_model=list[dict])
def get_compres(db: Session = Depends(get_db)):
    return compres.get_all_compres(db)

@app.get("/compres/{id}", response_model=dict)
def get_compra(id: int, db: Session = Depends(get_db)):
    return compres.get_compra_by_id(id, db)

@app.put("/compres/{id}", response_model=dict)
def update_compra(
    id: int,
    Data_Compra: str = Form(None),
    Proveidor: str = Form(None),
    Producte_Compra: str = Form(None),
    Quantitat: int = Form(None),
    Preu_Unitari: float = Form(None),
    Total: float = Form(None),
    Estat_Comanda: str = Form(None),
    db: Session = Depends(get_db)
):
    return compres.update_compra(id, Data_Compra, Proveidor, Producte_Compra, Quantitat, Preu_Unitari, Total, Estat_Comanda, db)

@app.delete("/compres/{id}", response_model=dict)
def delete_compra(id: int, db: Session = Depends(get_db)):
    return compres.delete_compra(id, db)


