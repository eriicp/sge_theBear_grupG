from email.policy import default
from math import trunc

from markdown_it.rules_block import table
from sqlalchemy.sql.operators import truediv
from sqlmodel import SQLModel, Field

class User(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    nom:str
    email:str