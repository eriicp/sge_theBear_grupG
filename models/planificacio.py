from sqlmodel import SQLModel, Field
from typing import Optional

class Planificacio(SQLModel, table=True):
    Id_Planificacio: Optional[int] = Field(default=None, primary_key=True)
    Projecte: str
    Tasca: str
    Responsable: int
    Data_Inici: str
    Data_Fi: str
    Estat_Tasca: str
    Material_Utilitzat: Optional[str] = None
    Comentaris: Optional[str] = None
