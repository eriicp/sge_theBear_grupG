from sqlmodel import SQLModel, Field
from typing import Optional

class PuntDeVenda(SQLModel, table=True):
    Id_Punt: Optional[int] = Field(default=None, primary_key=True)
    Nom_Punt: str
    Producte: str
    Quantitat: int
    Preu_Total: float
    Metode_Pagament: str
    Tiquet_Email: bool
    Data_Venda: str
