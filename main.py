from fastapi import FastAPI, Depends, HTTPException, Form
from sqlmodel import SQLModel, create_engine, Session
from dotenv import load_dotenv
import os

from services import planificacio, punts_de_venda

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