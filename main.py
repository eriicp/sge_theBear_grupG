from fastapi import FastAPI, Depends, HTTPException, Form
from sqlmodel import SQLModel, create_engine, Session
from dotenv import load_dotenv
import os
from services import costos, compres

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

# PARTE HUGO

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

# FINAL HUGO
