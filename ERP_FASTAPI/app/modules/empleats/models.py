from pydantic import BaseModel
from typing import Optional

class Empleat(BaseModel):
    id: int
    nom: str
    cognom: str
    email: str
    telefon: Optional[str] = None
    data_ingres: Optional[str] = None

class EmpleatCreate(BaseModel):
    nom: str
    cognom: str
    email: str
    telefon: Optional[str] = None

class EmpleatUpdate(BaseModel):
    nom: Optional[str] = None
    cognom: Optional[str] = None
    email: Optional[str] = None
    telefon: Optional[str] = None
    data_ingres: Optional[str] = None