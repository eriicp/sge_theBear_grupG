from sqlmodel import SQLModel, Field
from typing import Optional

class Event(SQLModel, table=True):
    Id_Event: Optional[int] = Field(default=None, primary_key=True)
    Nom_Event: str
    Data_Event: str
    Hora_Event: str
    Ubicacio_Event: str
    Organitzador_Event: int
    Estat_Event: str
    Entrades_Disponibles: int
    Privat: bool
