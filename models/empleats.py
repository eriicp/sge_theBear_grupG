from sqlmodel import SQLModel, Field
from typing import Optional

class Empleat(SQLModel, table=True):
    Id_Empleat: Optional[int] = Field(default=None, primary_key=True)
    Nombre_Empleat: str
    Puesto_Empleat: str
    Departament_Empleat: str
    Email_Empleat: str
    Telefon_Empleat: str
    Id_Gerent_Empleat: Optional[int] = None
