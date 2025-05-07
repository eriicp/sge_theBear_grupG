from sqlmodel import SQLModel, Field
from typing import Optional

class Reunio(SQLModel, table=True):
    Id_Reunio: Optional[int] = Field(default=None, primary_key=True)
    Nom_Reunio: str
    Data_Reunio: str
    Hora_Inici: str
    Hora_Fi: str
    Ubicacio_Reunio: str
    Etiquetes: Optional[str] = None
    Recurrencia: bool = False
