from sqlmodel import SQLModel, Field
from typing import Optional

class Compra(SQLModel, table=True):
    Id_Compra: Optional[int] = Field(default=None, primary_key=True)
    Data_Compra: str
    Proveidor: str
    Producte_Compra: str
    Quantitat: int
    Preu_Unitari: float
    Total: float
    Estat_Comanda: str
