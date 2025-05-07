from sqlmodel import SQLModel, Field
from typing import Optional

class Venda(SQLModel, table=True):
    Id_Venda: Optional[int] = Field(default=None, primary_key=True)
    Data_Venda: str
    Client_Venda: str
    Producte_Venda: str
    Quantitat: int
    Preu_Unitari: float
    Total: float
    Metode_Pagament: str
    Id_Punt: int
