from fastapi import FastAPI, Depends
from sqlalchemy import result_tuple
from sqlalchemy.testing.plugin.plugin_base import engines
from sqlmodel import SQLModel,create_engine, Session
from dotenv import load_dotenv
from services import user
import os
from typing import List
from fastapi import FastAPI
from services import read
app = FastAPI()

@app.get("/root", response_model=List[dict])
async def read_root():
    result = read.registre()
    return result
load_dotenv()
DATABASE_URL = os.getenv("DATABASE_URL")
engine = create_engine(DATABASE_URL)
SQLModel.metadata.create_all(engine)
def get_db():
    db = Session(engine)
    try:
        yield db
    finally:
        db.close()

@app.get("/users/", response_model= dict)
def read_user(db:Session=Depends(get_db)):
    result = user.get_all_users(db)
    return result




@app.post("/users/", response_model= list[dict])
def crate_user(name:str, email:str, db:Session=Depends(get_db)):
    result = user.add_new_user(name, email, db)
    return result
