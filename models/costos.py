from sqlmodel import SQLModel, Field
from typing import Optional

class Cost(SQLModel, table=True):
    Id_Cost: Optional[int] = Field(default=None, primary_key=True)
    Descripcio: str
    Categoria: str
    Quantitat: float
    Data_Cost: str
    Pagat_Per: int
